class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        counter = 0
        for num in nums:

            if target - num in dict:
                return [dict[target - num], counter]
            dict[num] = counter
            counter += 1


