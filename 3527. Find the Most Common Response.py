class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counts={}
        for day in responses:
            unique_response = set()
            for response in day:
                if response not in unique_response:
                    counts[response] = counts.get(response, 0) +1
                    unique_response.add(response)
        res = ""
        max_count = 0

        for word, count in counts.items():
            if count > max_count:
                res, max_count = word , count
            elif count == max_count:
                if word < res:
                    res = word
        return res

