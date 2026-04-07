class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        result = []
        stack = []
    
        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))
            if i == len(pattern) or pattern[i]=="I":
                while stack:
                    result.append(stack.pop())
                    
        return "".join(result)
            