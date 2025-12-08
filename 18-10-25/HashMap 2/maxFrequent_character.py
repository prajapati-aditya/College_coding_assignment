class Solution:
    def getMaxOccurringChar(self, s):
        #code here
        freq = {}
        for char in s :
            if char in freq :
                freq[char] += 1
            else :
                freq[char] = 1
        res  = " "
        a = -1
        for char , num in freq.items() :
            if num > a or (num == a and char < res ) :
                res = char
                a = num
        return res