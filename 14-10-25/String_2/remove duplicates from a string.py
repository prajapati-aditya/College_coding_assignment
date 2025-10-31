s ="aditya"

def remove(s) :
    freq=[0]*26
    for str in s :
        if freq[ord(str) - ord("a")] == 0 :
            freq[ord(str) - ord("a")] = 1
    res = ""
    for num in range (len(freq)) :
        if freq[num] == 1:
            res += chr(ord("a")+num)
    print(res) 
remove(s)
