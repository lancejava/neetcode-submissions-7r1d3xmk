class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)

        total = (high - low + 1) * (high + low) // 2
        
        return total - sum(nums)