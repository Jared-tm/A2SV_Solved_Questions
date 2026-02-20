n  = int(input())
s = list(map(int, input().split()))
s.sort()
if n%2 == 0:
    print (s[(n//2) -1])
else:
    print(s[(n//2)])

