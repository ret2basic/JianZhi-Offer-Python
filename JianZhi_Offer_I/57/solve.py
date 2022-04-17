class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            result = nums[left] + nums[right]
            if result == target:
                return [nums[left], nums[right]]
            elif result < target:
                left += 1
            elif result > target:
                right -= 1

        return []