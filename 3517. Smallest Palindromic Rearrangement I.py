s = "aaccd"
n = len(s)
s= (sorted(s))
print(s)
res = ""

for char in s:
    res += char
print(res)

"""if len(res) % 2 ==0:
    print(res + res[::-1])
else:
    print(res+ res[::-1] )"""