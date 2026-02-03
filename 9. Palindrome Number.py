class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        if x<0:
            return False
        rev=0
        while x:
            rev = rev*10 + x%10
            x//=10
        return num==rev
         