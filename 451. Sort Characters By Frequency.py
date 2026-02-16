class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_count  = {k: v for k, v in sorted(count.items(), key=lambda x: x[1], reverse=True)}

        res = ""
        for ch , freq in sorted_count.items():
            res += ch*freq
        
        return res