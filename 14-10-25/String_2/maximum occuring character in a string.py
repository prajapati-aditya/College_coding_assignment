s = "apple"
freq = { }
for str in s :
    if str in freq :
        freq[str] += 1
    else :
        freq[str] = 1
print (freq)

maxi = max(freq.values())
print(maxi)

for char, val in freq.items() :
    if val == maxi:
        print(char)
        break
