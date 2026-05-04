class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target = len(graph)-1
        results = []
        
        def backtrack(curr_node, path):
            if curr_node == target:
                results.append(list(path))
                return
            for neighbor in graph[curr_node]:
                path.append(neighbor)
                backtrack(neighbor, path) 
                path.pop()
        
        backtrack(0, [0])
        return results