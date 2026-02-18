class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split(" "))
        if len(pattern) != len(s):
            return False
        else:
            hashmap={}
            is_matching = True

            for i in range(len(s)):
                word = s[i]
                ch = pattern[i]
                if ch in hashmap:
                    if hashmap[ch] != word:
                        is_matching = False
                        break
                else:
                    if word in hashmap.values():
                        is_matching = False
                        break
                    hashmap[ch] = word
            return is_matching