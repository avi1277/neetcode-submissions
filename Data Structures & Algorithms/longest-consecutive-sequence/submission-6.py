class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        max_count = 0

        for num in nums:
            count = 1
            next = num + 1
            while next in check:
                count += 1
                next += 1
            if count > max_count:
                max_count = count

        return max_count