class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colors = [0] * n 
      
        for i in range(n):
            if colors[i] != 0:
                continue
            
            queue = deque([i])
            colors[i] = 1
            
            while queue:
                node = queue.popleft()
                
                for neighbor in graph[node]:
                    if colors[neighbor] == colors[node]:
                        return False
                  
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)
                        
        return True
        