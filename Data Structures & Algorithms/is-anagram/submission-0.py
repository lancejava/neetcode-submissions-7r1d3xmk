class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = {}

        for c in s:
            sCounter[c] = sCounter.get(c, 0) + 1
        
        tCounter = {}

        for c in t:
            tCounter[c] = tCounter.get(c, 0) + 1
        
        return sCounter == tCounter