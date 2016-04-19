from django.core.management.base import BaseCommand, CommandError
from antonymapp.models import WordPair1, WordPair2
import math

word_pairs1 = WordPair1.objects.all()
word_pairs2 = WordPair2.objects.all()

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

	def levene(self, word_pair1, word_pair2):
		N = [0, 0]
		N[0] = word_pair1.ones + word_pair1.two + word_pair1.three + word_pair1.four + word_pair1.five 
		N[1] = word_pair2.ones + word_pair2.two + word_pair2.three + word_pair2.four + word_pair2.five 
		Y_1 = self.freq_to_list(word_pair1)
		Y_2 = self.freq_to_list(word_pair2)
		YZ_1 = Y_1
		YZ_2 = Y_2
		YZ_1[:] = [abs(float(x) - (sum(Y_1) / float(len(Y_1)))) for x in YZ_1]
		YZ_2[:] = [abs(float(x) - (sum(Y_2) / float(len(Y_2)))) for x in YZ_2]
		Z = [YZ_1] + [YZ_2]
		Z_sum = 0
		for Y in Z:
			for z in Y:
				Z_sum += z
		Z_dot_dot = float(Z_sum)/float(sum(N))
		Z_dot = []
		for Y in Z:
			Z_dot += [(sum(Y) / float(len(Y_1)))]

		nominator = 0
		for i in range(0,2):
			nominator += N[i]*((Z_dot[i]-Z_dot_dot)**2)
		denominator = 0
		for i in range(0,2):
			for j in range(0,len(Z[i])):
				denominator += (Z[i][j]-Z_dot[i])**2
		if denominator != 0:
			W = (sum(N)-2)*nominator/denominator
		else :
			W = "denominator = 0"

		print W

	def std_dev(self, one, two, three, four, five, n):
		return math.sqrt(self.variance(one,two,three,four,five,n))

	def variance(self, one, two, three, four, five, n):
		sum_square = one + 4*two + 9*three + 16*four + 25*five
		square_sum = (one + 2*two + 3*three + 4*four + 5*five)**2
		variance = (sum_square - square_sum/n)/(n-1)
		return variance 

	def _for_pairs(self, word_pairs):
		for pair in word_pairs :
			word1 = pair.word1
			word2 = pair.word2 
			one = float(pair.ones)
			two = float(pair.two)
			three = float(pair.three)
			four = float(pair.four)
			five = float(pair.five)
			n = float(one+two+three+four+five)
			if n>1:
				mean = (one + 2*two + 3*three + 4*four + 5*five)/(one+two+three+four+five)
				std = self.std_dev(one, two, three, four, five, n)
				s = "" + word1[:5] +"\t"+ word2[:5] +"\t"+  str(int(one)) +"\t"+  str(int(two)) +"\t"+  str(int(three)) +"\t"+  str(int(four)) +"\t"+  str(int(five)) +"\t"+  str(int(n)) +"\t"+  str(round(mean,5)) +"\t\t"+  str(round(std,5))
				print(s)

	def handle(self, *args, **options):
		print("\n\n")
		print("word1 \t word2 \t one \t two \t three \t four \t five \t n \t mean \t\t std_dev \n")
		self._for_pairs(word_pairs1)
		self._for_pairs(word_pairs2)
		print("\n\n")
		for i in range(2,26):
			self.levene(word_pairs1.get(word_number=1),word_pairs1.get(word_number=i))