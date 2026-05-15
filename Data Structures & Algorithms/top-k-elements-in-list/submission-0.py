class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num, amount in count.items():
            freq[amount].append(num)
        
        ans = []
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans