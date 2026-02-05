matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=set()
        losers_dict={}
        for winner,loser in matches:
            winners.add(winner)
            losers_dict[loser]=losers_dict.get(loser,0) +1
        abs_winner=[]
        lost_only_one=[]
        
        for player in winners:
            if player not in losers_dict:
                abs_winner.append(player)
            
        for player,lost in losers_dict.items():
            if lost ==1:
                lost_only_one.append(player)
        return([sorted(abs_winner),sorted(lost_only_one)])


            
        




