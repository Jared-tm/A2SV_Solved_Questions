numerals = {
            "I" :  1,
            "V" : 5,
            "IV": 4,
            "X" : 10,
            "IX": 9,
            "L" : 50,
            "XL": 40, 
            "C" : 100,
            "XC": 90,
            "D" : 500,
            "CD": 400,
            "M" : 1000,
            "CM":900
        }
s= "MCMXCIV"
value = 0
weird = set(["IV", "IX", "XL", "XC","CD", "CM"])
i = 0
while i < len(s):
    if s[i:i+2] in weird:
        char = s[i:i+2]
        i +=2
    else:
        char = s[i]
        i +=1
    value += numerals[char]
    print(value)
        