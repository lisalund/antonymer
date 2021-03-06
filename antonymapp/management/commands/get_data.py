from __future__ import print_function
from django.core.management.base import BaseCommand, CommandError
from antonymapp.models import WordPair1, WordPair2
import math
from scipy.stats import levene, wilcoxon, chi2_contingency
from numpy import mean, std
from scipy import stats

word_pairs1 = WordPair1.objects.all()
word_pairs2 = WordPair2.objects.all()
word_pairs = [word_pairs1] + [word_pairs2]

class Command(BaseCommand):

	def freq_to_list(self, word_pair):
		Y = []
		for i in range(0,word_pair.ones):
			Y += [1]
		for i in range(0,word_pair.two):
			Y += [2]
		for i in range(0,word_pair.three):
			Y += [3]
		for i in range(0,word_pair.four):
			Y += [4]
		for i in range(0,word_pair.five):
			Y += [5]
		return Y

	def handle(self, *args, **options):
		print("\n\n")
		print("word1 \t word2 \t n \t mean \t std_dev")
		print("\n")
		mean1 = []
		mean2 = []
		for j in range(0,2):
			for i in range(1,26):
				word = word_pairs[j].get(word_number=i)
				word1 = word.word1[:5]
				word2 = word.word2[:5]
				Y_1 = self.freq_to_list(word)
				n = len(Y_1)
				mean_value = mean(Y_1)
				std_value = std(Y_1)
				if j == 0:
					mean1 += [mean_value]
				else:
					mean2 += [mean_value]
				print("%s \t %s \t %d \t %.5f \t %.5f" % (word1, word2, n, mean_value, std_value))

		W, p = stats.wilcoxon(mean1,mean2)
		print()
		print("Wilcoxon returns W = %.5f, and p = %.5f" % (W,p))
		print("Can not reject null hypothesis since p>0.1")
		print()
		print("Matrix for levenes test W-value")
		for i in range(1,26):
			pair1 = word_pairs[0].get(word_number=i)
			word1 = pair1.word1[:4]
			word2 = pair1.word2[:4]
			print(word1 + " " + word2 + " ", end="")
			for j in range(1,26):
				pair2 = word = word_pairs[0].get(word_number=j)
				Y_1 = self.freq_to_list(pair1)
				Y_2 = self.freq_to_list(pair2)
				W, p = levene(Y_1, Y_2)
				print(' {0:.2f}'.format(W), end="")
			print()

		print()
		print("Matrix for levenes test p-value")
		for i in range(1,26):
			pair1 = word_pairs[0].get(word_number=i)
			word1 = pair1.word1[:4]
			word2 = pair1.word2[:4]
			print(word1 + " " + word2 + " ", end="")
			for j in range(1,26):
				pair2 = word = word_pairs[0].get(word_number=j)
				Y_1 = self.freq_to_list(pair1)
				Y_2 = self.freq_to_list(pair2)
				W, p = levene(Y_1, Y_2)
				print(' {0:.2f}'.format(p), end="")
			print()

		## Time for chi squared
		pairs = []
		pairs += [word_pairs[0].get(word1="kort",word2="kolossal")]
		pairs += [word_pairs[0].get(word1="smal",word2="bred")]
		pairs += [word_pairs[0].get(word1="liten",word2="enorm")]
		pairs += [word_pairs[0].get(word1="kort",word2="stor")]
		pairs += [word_pairs[0].get(word1="futtig",word2="bred")]
		pairs += [word_pairs[0].get(word1="liten",word2="tung")]
		pairs += [word_pairs[1].get(word1="bred",word2="futtig")]
		pairs += [word_pairs[1].get(word1="enorm",word2="liten")]
		pairs += [word_pairs[1].get(word1="bred",word2="liten")]
		pairs += [word_pairs[1].get(word1="bred",word2="kort")]
		pairs += [word_pairs[1].get(word1="kolossal",word2="ynklig")]
		pairs += [word_pairs[1].get(word1="stor",word2="futtig")]
		pairs += [word_pairs[1].get(word1="enorm",word2="smal")]
		pairs += [word_pairs[1].get(word1="tung",word2="smal")]
		pairs += [word_pairs[1].get(word1="bred",word2="smal")]
		extreme = 0
		non_extreme = 0
		total = 0
		for pair in pairs:
			pair_values = self.freq_to_list(pair)
			for num in pair_values:
				total += 1
				if (num==1 or num==5):
					extreme += 1
				else:
					non_extreme += 1
		print()
		print("data for chi square test")
		print("extreme values: "+ str(extreme))
		print("non extreme values: "+ str(non_extreme))
		print("total"+ str(total))

		C, p,ddof, expected = chi2_contingency([[extreme, 497],[non_extreme, 864]])
		print(C)
		print(p)
		print(ddof)
		print(expected)
#		print("chisquare returns C = %.5f, and p = %.5f" % (C,p))