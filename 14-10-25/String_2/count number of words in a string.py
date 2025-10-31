string = "Hello World "
# output = 2

def count_word(s) :
    spc = 0
    for str in s :
        if str  == " " :
            spc += 1
    return spc+1
        

print (count_word(string.strip()) )