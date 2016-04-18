from django.core.management.base import BaseCommand
from antonymapp.models import WordPair1, WordPair2

words1 = ["liten", "smal", "kort", "futtig", "ynklig"];
words2 = ["stor", "bred", "kolossal", "tung", "enorm"];

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_pairs(self):
        for word1 in words1:
            for word2 in words2:
                pair = WordPair1(word1=word1, word2=word2)
                pair.save()
                pair = WordPair2(word1=word2, word2=word1)
                pair.save()

    def handle(self, *args, **options):
        self._create_pairs()