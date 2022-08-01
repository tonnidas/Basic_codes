# Problem: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = dict() # frequency table 
        for c in s: 
            if c not in freq:
                freq[c] = 0
            freq[c] = freq[c] + 1
        print(freq)
        
        ans = 0
        seen = set()
        print(freq.values(), "=")
        
        for k in freq.values(): 
            print("seen = ", seen, "k = ", k)
            # while k in seen: 
            t = True
            while t:
                if k in seen:
                    print("tonni")
                    k = k - 1 
                    ans = ans + 1
                else:
                    t = False
            if k > 0: 
                seen.add(k)
                print("seen = ", seen)
                
        return ans 