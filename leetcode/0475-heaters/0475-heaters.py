class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        
        min_radius = 0
        heater_p = 0
        n = len(heaters)
        
        for house in houses:
            while (heater_p+1<n and abs(heaters[heater_p+1] -house)<= abs(heaters[heater_p]-house)):
                heater_p += 1
            dist = abs(heaters[heater_p] - house)
            if dist > min_radius:
                min_radius = dist
                
        return min_radius
        