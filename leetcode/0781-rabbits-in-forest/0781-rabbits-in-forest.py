class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int` v
        """
        freq = Counter(answers)
        min_rabbits = 0  
        
        for rabbit in answers:
            if len(freq) == 0:
                break
            elif rabbit in freq:
                freq[rabbit] -= 1  
                min_rabbits += 1 + rabbit


                if freq[rabbit] - rabbit <= 0:
                    del freq[rabbit]
                else:
                    freq[rabbit] = freq[rabbit] - rabbit

        return min_rabbits
        