t = int(input())
for _ in range(t):
    s = input()
    res = set()

    n = len(s)
    fast = 0
    slow = fast

    while fast < n:
        while fast<n and s[fast] == s[slow]:
            fast += 1
        if (fast - slow )%2 == 1:
            res.add(s[slow])
        slow=fast

    res = sorted(list(res))
    print("".join(res))


