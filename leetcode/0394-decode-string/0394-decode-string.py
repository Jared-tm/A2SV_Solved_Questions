class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        _str = ""
        num = 0

        for char in s:
            if char.isdigit():
                num = 10*num + int(char)
            elif char == "[":
                stack.append((_str, num))
                num=0
                _str = ""
            elif char == "]":
                prev_str, n = stack.pop()
                _str = prev_str + (_str*n)
            else:
                _str += char
        

        return _str


