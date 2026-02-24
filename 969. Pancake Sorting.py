class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        res = []
        n = len(arr)

        for i in range (n-1, -1 , -1):
            _max = arr[0]
            idx=0
            for j in range (i+1):
                if arr[j] >= _max:
                    idx = j
                    _max = arr[j]
            
            if idx == i:
                continue
            elif idx == 0:
                res.append(i+1)
                arr[:i+1] = arr[:i+1][::-1]
            else:
                res.append(idx+1)
                arr[:idx+1] = arr[:idx+1][::-1]

                res.append(i+1)
                arr[:i+1] = arr[:i+1][::-1]

        return res



            
        
