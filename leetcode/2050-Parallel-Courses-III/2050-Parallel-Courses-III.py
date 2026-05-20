class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        
        for prev, next_course in relations:
            graph[prev].append(next_course)
            in_degree[next_course] += 1
       
        max_time = [0] * (n + 1)
        queue = deque()
        
        for i in range(1, n + 1):
            max_time[i] = time[i - 1]
            if in_degree[i] == 0:
                queue.append(i)
     
        while queue:
            curr = queue.popleft()
            
            for next_course in graph[curr]:
               
                new_completion_time = max_time[curr] + time[next_course - 1]
                if new_completion_time > max_time[next_course]:
                    max_time[next_course] = new_completion_time
                
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
                    
                
        return max(max_time)