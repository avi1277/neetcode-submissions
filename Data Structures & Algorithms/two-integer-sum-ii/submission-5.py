class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1

        for l in range(len(numbers)):
            for r in range(len(numbers) - 1):
                if numbers[l] + numbers[r] == target and numbers[l] != numbers[r]:
                    if r > l:
                        return [l + 1, r + 1]
                    else:
                        return [r + 1, l + 1]
                r += 1
            l += 1