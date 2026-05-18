class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for word in strs:
            length = str(len(word))
            output = output + length + "!" + word
        return output

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "!":
                j = j + 1
            length = int(s[i:j])
            decoded.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return decoded