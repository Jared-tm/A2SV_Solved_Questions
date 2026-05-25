class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocation = []
        
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
             
            if climb <= 0:
                continue
                
            heapq.heappush(ladder_allocation, climb)
            
            if len(ladder_allocation) > ladders:
                smallest_climb = heapq.heappop(ladder_allocation)

                bricks -= smallest_climb
            if bricks < 0:
                return i

        return len(heights) - 1