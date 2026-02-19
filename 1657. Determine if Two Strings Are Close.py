class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1Count = Counter(word1)
        word2Count = Counter(word2)

        if set(word1Count.keys()) != set(word2Count.keys()):
            return False

        return sorted(word1Count.values()) == sorted(word2Count.values() )
