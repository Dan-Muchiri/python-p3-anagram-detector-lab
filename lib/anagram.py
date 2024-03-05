# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        anagrams = []
        for candidate in candidates:
            candidate_lower = candidate.lower()
            if self.word != candidate_lower and sorted(self.word) == sorted(candidate_lower):
                anagrams.append(candidate)
        return anagrams
