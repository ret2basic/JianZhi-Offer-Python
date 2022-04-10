class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(value):
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= value:
                    low = mid + 1
                else:
                    high = mid - 1
        
            return low
        
        return binary_search(target) - binary_search(target - 1)