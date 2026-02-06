class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        word_pos={w:i for i ,w in enumerate (list1)}
        least_sum=[]
        min_sum=float("inf")
        for i,w in enumerate(list2):
            if w in list1:
                if word_pos[w] + i < min_sum:
                    least_sum = [w]
                    min_sum = min(min_sum, word_pos[w] + i)
                elif word_pos[w] + i == min_sum:
                    least_sum.append(w)
        return least_sum
                


                