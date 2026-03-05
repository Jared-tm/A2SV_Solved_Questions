class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {}
        end = 0
        res = []
        start = 0
        for i, char in enumerate(s):
            last[char] = i
        for i, char in enumerate(s):
            end = max(end, last[char])
            if i == end:
                res.append(end-start+1)
                start = end + 1
        return res