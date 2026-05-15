class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        counter = 0
        for num in nums:
            if num in index:
                if index[num] != counter:
                    return [index[num], counter]
            needed = target - num
            index[needed] = counter
            counter = counter + 1

            