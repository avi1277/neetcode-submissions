class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        seen = set()
        counter = 0
        maxCount = 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] in s[i:j]:
                    break
                else:
                    counter = len(s[i:j+1])
                    if maxCount < counter:
                        maxCount = counter

        return maxCount
