class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransome_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for char in set(ransome_count.keys()):
            if char not in magazine:
                return False
            if ransome_count[char] > magazine_count[char]:
                return False
        return True