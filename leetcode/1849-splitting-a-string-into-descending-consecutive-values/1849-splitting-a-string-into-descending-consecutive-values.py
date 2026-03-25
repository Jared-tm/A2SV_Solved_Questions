class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def split(path, i):
            if i == len(s):
                return len(path) >= 2
            for j in range(i, len(s)):
                val = int(s[i : j + 1])
                if not path or val == path[-1] - 1:
                    path.append(val)
                    if split(path, j + 1):
                        return True
                    path.pop()
                elif path and val >= path[-1]:
                    break
                    
            return False          
        
        return split([], 0)