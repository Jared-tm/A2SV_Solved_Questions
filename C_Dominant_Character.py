t = int(input())
for _ in range (t):

    n = int (input())
    s= input()
    ans=float('inf')

    for left in range(n-1):
        if s[left] == "a":

            for right in range(left+1,min(left+7,n)):
                if s[right] == "a":

                    sub_string = s[left:right+1]
                    count_a = sub_string.count('a')
                    count_b = sub_string.count('b')
                    count_c = sub_string.count('c')

                    if count_a > count_b and count_a >  count_c:
                        ans = min(ans,right-left+1)
                    
                    if ans == 2:
                        break
            if ans ==2:
                break
                             
    print(ans if ans != float("inf") else -1)
  
            



            

