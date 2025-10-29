s = "take12% *&u ^$#forward "
res=""
p = 0
while p < len(s) :
    ch = s[p]
    if ch.isalpha() :
        res+=ch 
    p+=1
print(res)
    

