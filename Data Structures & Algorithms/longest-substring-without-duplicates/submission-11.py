class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        left, right = 0, 0
        maxCount = 1
        seen = set()
        while right < len(s):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxCount = max(right - left + 1, maxCount)
            right += 1
        return maxCount
