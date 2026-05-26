import math

def solve():
    s1 = input().strip()
    s2 = input().strip()

    target = s1.count('+') - s1.count('-')
    
    current = s2.count('+') - s2.count('-')
    u_count = s2.count('?')
    
    delta = target - current

    if (u_count + delta) % 2 != 0 or abs(delta) > u_count:
        print(f"{0.0:.12f}")
        return
        
    c_plus = (u_count + delta) // 2

    favorable_ways = math.comb(u_count, c_plus)
    total_ways = 1 << u_count # 2^u_count
    
    prob = favorable_ways / total_ways
    print(f"{prob:.12f}")

if __name__ == '__main__':
    solve()