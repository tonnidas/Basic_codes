# Problem: https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in range(len(words)):
            num = words[i]
            if num == s[0:len(num)]:
                count = count + 1
        return count 