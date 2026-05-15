class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        table_s = {}
        table_t = {}

        for ch in s:
            if ch not in table_s:
                table_s[ch] = 1
            else:
                table_s[ch] = table_s[ch] + 1
        for ch in t:
            if ch not in table_t:
                table_t[ch] = 1
            else:
                table_t[ch] = table_t[ch] + 1
                

        return table_s == table_t
        