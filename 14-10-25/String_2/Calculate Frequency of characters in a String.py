inp ="articles"
#Output: a1 c1 e1 i1 l1 r1 s1 t1 
freq=[0]*26
for str in inp :
    freq[ord(str) - ord("a")] +=1 
print(freq) 
for i in range (len(freq)) :
    if freq[i] != 0:
        x = chr(i+ord("a") )
        y = freq[i] 
        print ( f"{x}{y}", end =" " )
    