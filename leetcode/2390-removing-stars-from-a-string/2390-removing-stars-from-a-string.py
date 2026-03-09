class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for c in s:
            if c != "*":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
        