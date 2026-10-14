class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_max = 0
        for i in nums:
            if i == 1:
                curr_max += 1
                max_ones = max(max_ones, curr_max)
            else:
                curr_max = 0
        return max_ones

        