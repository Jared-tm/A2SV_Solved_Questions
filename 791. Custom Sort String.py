class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        for char in order:
            for letter in s:
                if char == letter:
                    res += letter
        
        for lett in s:
            if lett not in order:
                res += lett
        
        return res
                
