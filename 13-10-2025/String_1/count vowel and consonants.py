str = "India won the cricket match"

def count (str) :
    p = 0
    vowel = set ("aeiouAEIOU")
    v_count = 0
    c_count = 0
    
    while p < len(str) :
        if str[p] == " " :
            p += 1
        if str[p] in vowel :
            v_count+=1 
            p+=1
        else :
            c_count+=1
            p+=1
    print (v_count)
    print (c_count)
    
count(str)
        
         
        