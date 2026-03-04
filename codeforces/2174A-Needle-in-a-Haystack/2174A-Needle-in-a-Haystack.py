from collections import Counter

def solve():
    s = input()
    t = input()
    count_t = Counter(t)
    count_s = Counter(s)

    for char in count_s:
        if count_t[char] < count_s[char]:
            print("Impossible")
            return

    res = []
    s_ptr = 0
    left = Counter(t)
    for char in s:
        left[char] -= 1

    for _ in range(len(t)):
        for char_code in range(97, 123):
            char = chr(char_code)
            
            if count_t[char] > 0:
                if s_ptr < len(s) and s[s_ptr] == char:
                    if s[s_ptr:] < char + s[s_ptr:]:
                        res.append(char)
                        count_t[char] -= 1
                        s_ptr += 1
                        break
                    elif left[char] > 0:
                        res.append(char)
                        count_t[char] -= 1
                        left[char] -= 1
                        break
                    else:
                        res.append(char)
                        count_t[char] -= 1
                        s_ptr += 1
                        break
                
                elif left[char] > 0:
                    res.append(char)
                    count_t[char] -= 1
                    left[char] -= 1
                    break
                    
    print("".join(res))

n = int(input())
for _ in range(n):
    solve()