MAX_TEMP = 200005
 
def solve():
 
    n, k, q = map(int, input().split())
    diff = [0] * (MAX_TEMP + 2)
 
    for _ in range(n):
        l, r = map(int, input().split())
        diff[l] += 1
        diff[r + 1] -= 1
 
    admissible = [0] * (MAX_TEMP + 1)
    current_recipes = 0
    for i in range(1, MAX_TEMP + 1):
        current_recipes += diff[i]
        if current_recipes >= k:
            admissible[i] = 1
        else:
            admissible[i] = 0
 
    pref = [0] * (MAX_TEMP + 1)
    for i in range(1, MAX_TEMP + 1):
        pref[i] = pref[i-1] + admissible[i]
 
    results = []
    for _ in range(q):
        a, b = map(int, input().split())
        results.append(str(pref[b] - pref[a-1]))
 
    print('\n'.join(results))
 
if __name__ == "__main__":
    solve()