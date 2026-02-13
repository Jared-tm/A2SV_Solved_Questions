def solve():
    n,x,k =map(int,input().split())
    s = input()

    pos = x
    time_to_first = -1

    for i in range(min(n,k)):
        pos += 1 if s[i] =="R" else -1
        if pos == 0:
            time_to_first = i + 1
            break
    if time_to_first == -1:
        print(0)
        return
    
    time_to_cycle = -1
    pos = 0
    for i in range(n):
        pos += 1 if s[i] =="R" else -1
        if pos == 0:
            time_to_cycle = i+1
            break
    
    ans = 1
    if time_to_cycle != -1:
        ans += (k-time_to_first) // time_to_cycle

    print(ans)
 
t = int(input())
for _ in range(t):
    solve()

