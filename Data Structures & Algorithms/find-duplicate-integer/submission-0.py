class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        max = 0
        dupes = set()

        for num in nums:

            if num in dupes:
                return num
            else:
                dupes.add(num)