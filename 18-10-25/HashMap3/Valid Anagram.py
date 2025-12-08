from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # creating dictionary using Counter
        dict_s=Counter(s)
        dict_t = Counter(t)

        # edge case
        if len(s) != len(t):
            return False
        
        return dict_t == dict_s