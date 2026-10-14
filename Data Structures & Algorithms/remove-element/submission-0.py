class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            num = nums[i]
            if num != val:
                nums[k] = num
                k += 1
        
        return k
        