class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left, right = 0, len(nums) - 1

        while (left < right):
            middle = (right - left) + left // 2
            result = min(nums[middle], result)

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        
        return min(result, nums[left])
            
            
