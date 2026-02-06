words = ["cat","bt","hat","tree"]
chars = "atach"
if not chars or not words:
    print(0)
len_good=0
chars_dict={}
for c in chars:
    chars_dict[c] = chars_dict.get(c,0) +1
for word in words:
    word_dict={}
    for l in word:
        word_dict[l] = word_dict.get(l,0) + 1
        good = True
        if word_dict[l] > chars_dict.get(l, 0):
            good = False
            break
    if good:
        len_good += len(word)
print(len_good)

        


            



