from django.core.management.base import BaseCommand, CommandError
from antonymapp.models import WordPair1, WordPair2
import math

word_pairs1 = WordPair1.objects.all()
word_pairs2 = WordPair2.objects.all()

class Command(BaseCommand):

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