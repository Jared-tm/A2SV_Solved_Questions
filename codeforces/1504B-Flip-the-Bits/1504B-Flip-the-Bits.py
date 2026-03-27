t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input().strip())
    b = list(input().strip())
    balance = [False] * n
    zeros = ones = 0
    
    for i in range(n):
        if a[i] == '0':
            zeros += 1
        else:
            ones += 1
        if zeros == ones:
            balance[i] = True

    flipped = False
    possible = True

    for i in range(n-1,-1,-1):
        cur = a[i]
        if flipped:
            cur = '1' if cur == '0' else '0'
        if cur != b[i]:
            if not balance[i]:
                possible = False
                break
            flipped = not flipped
    print("YES" if possible else "NO")