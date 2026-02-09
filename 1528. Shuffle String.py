class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=[""]*len(s)
        for i,char in enumerate(s):
            ans[indices[i]] = char
        return "".join(ans)
