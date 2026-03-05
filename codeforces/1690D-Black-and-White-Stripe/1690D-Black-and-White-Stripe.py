def solve():
    n,k = map(int, input().split())
    s = input()
 
    w_count = s[:k].count("W")
    ans = w_count
    for i in range(1,n-k+1):
        if s[i-1] == "W":
            w_count -= 1
        if s[i+k-1] == "W":
            w_count += 1
        
        ans = min(ans, w_count)
    print(ans)
    return

   
t = int(input())
for _ in range(t):
    solve()