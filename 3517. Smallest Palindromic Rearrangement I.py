class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)
        left = [] 
        middle = ""
        for char, freq in sorted(count.items()):
            left.append(char * (freq // 2)) 
            if freq % 2 == 1:
                middle = char
        left = "".join(left) 
        return left+ middle + left[::-1]
                