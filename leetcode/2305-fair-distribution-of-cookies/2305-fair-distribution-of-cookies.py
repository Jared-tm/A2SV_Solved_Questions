class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        distribution = [0]*k
        self.result = float('inf')
        cookies.sort(reverse=True)
        
        def backtrack(cookie_i):
    
            if cookie_i == len(cookies):
                self.result = min(self.result, max(distribution))
                return
    
            if max(distribution) >= self.result:
                return
            
            for i in range(k):
                if i > 0 and distribution[i] == distribution[i-1]:
                    continue
                
                distribution[i] += cookies[cookie_i]
                backtrack(cookie_i + 1)
                distribution[i] -= cookies[cookie_i]
                
        backtrack(0)
        return self.result