class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int` v
        """
        freq = Counter(answers) 
        min_rabbits = 0
        for ans, count in freq.items():
            group_size = ans + 1 
            num_groups = math.ceil(count / float(group_size)) 
            min_rabbits += num_groups * group_size
            
        return int(min_rabbits)