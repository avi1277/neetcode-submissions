class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        
        for word in strs:
            frequency = [0] * 26
            for ch in word:
                index = self.convert_to_index(ch)
                frequency[index] = frequency[index] + 1
            key = tuple(frequency)
            if key in words:
                words[key].append(word)
            else:
                words[key] = [word]
        ans = []
        for key in words:
            ans.append(words[key])
        return ans
    def convert_to_index(self, letter: str) -> int:
        chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        index = 0
        for ch in chars:
            if ch == letter:
                return index
            index = index + 1



                    

                
        