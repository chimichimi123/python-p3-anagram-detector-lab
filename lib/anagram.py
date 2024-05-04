class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.word_sorted = sorted(self.word)

    def match(self, words):
        return [word for word in words if sorted(word.lower()) == self.word_sorted and word.lower() != self.word]