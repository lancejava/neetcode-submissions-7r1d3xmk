class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}

        for i in range(len(nums)):
            need = target - nums[i]
            if need in seenNums:
                return [seenNums[need] , i]
            seenNums[nums[i]] = i