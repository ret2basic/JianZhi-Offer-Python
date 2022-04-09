class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(target_num):
            left, right = 0, len(nums) - 1
            while left <= right:
                m = (left + right) // 2
                if nums[m] <= target_num:
                    left = m + 1
                else:
                    right = m - 1
            return left
        
        return helper(target) - helper(target - 1)
