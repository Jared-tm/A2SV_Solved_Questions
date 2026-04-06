class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.result = ""
        self.count = 0
        
        def backtrack(curr_str):
            if len(curr_str) == n:
                self.count += 1
                if self.count == k:
                    self.result = curr_str
                return

            for char in ['a', 'b', 'c']:
                if not curr_str or curr_str[-1] != char:
                    backtrack(curr_str + char)
                    if self.result:
                        return

        backtrack("")
        return self.result
        