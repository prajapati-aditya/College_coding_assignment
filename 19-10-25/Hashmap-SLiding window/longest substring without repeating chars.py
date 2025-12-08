s = "pwwkew"
r = l = 0
chars_window = {}
longest = 0 
for ch in s :
    if ch not in chars_window and chars_window[ch] >= l :
        l += chars_window[ch] + 1
    
    chars_window[ch] = r 
    r += 1
    longest = max(longest,r-l+1)
print(longest) 
