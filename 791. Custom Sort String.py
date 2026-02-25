class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {}
        for idx , char in enumerate (order):
            order_map[char] = idx
            
        s = list(s)

      
        
        for i in range(len(s)-1):
            swapped = False
            for j in range(len(s)-i-1):
                if order_map.get(s[j+1], 1000) < order_map.get(s[j], 1000):
                    s[j], s[j+1] = s[j+1], s[j]
                    swapped = True
            if swapped == False:
                break
       
        return "".join(s)
                

if __name__ == "__main__":
    ord = "cba"
    sa = "abcd"
    print(Solution().customSortString(ord, sa))
