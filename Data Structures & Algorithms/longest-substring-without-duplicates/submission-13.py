class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        l, r = 0, 0
        maxCount = 1
        seen = set()

        while r < len(s):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])

            maxCount = max(r - l + 1, maxCount)
            r += 1
        return maxCount


            
