class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        s_char, t_char = {}, {}
        for i in range(len(s)):
            s_char[s[i]] = s_char.get(s[i], 0) + 1
        for j in range(len(t)):
            t_char[t[j]] = t_char.get(t[j], 0) + 1
        
        return s_char == t_char
        

