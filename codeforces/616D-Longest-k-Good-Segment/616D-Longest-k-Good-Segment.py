def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
 
    counts = [0] * 1000001
    left = 0
    unique_count = 0
    best_l, best_r = 1, 1
    max_len = -1
 
    for right in range(n):
        val_r = a[right]
        
        if counts[val_r] == 0:
            unique_count += 1
        counts[val_r] += 1
 
        while unique_count > k:
            val_l = a[left]
            counts[val_l] -= 1
            if counts[val_l] == 0:
                unique_count -= 1
            left += 1
 
        if right - left > max_len:
            max_len = right - left
            best_l, best_r = left + 1, right + 1
            
    print(f"{best_l} {best_r}")
 
if __name__ == "__main__":
    solve()