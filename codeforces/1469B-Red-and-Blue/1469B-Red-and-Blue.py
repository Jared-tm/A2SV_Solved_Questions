def solve():
    n = int(input())
    ar = list(map(int, input().split()))
    m = int(input())
    ab = list(map(int, input().split()))

    _red = 0
    _blue = 0

    curr = 0
    for num in ar:
        curr += num
        _red = max(_red, curr)
    curr = 0
    for num in ab:
        curr += num
        _blue = max(_blue, curr)
    print( _blue + _red)
    return


t = int(input())
for _ in range(t):
    solve()