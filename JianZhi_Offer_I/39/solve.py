class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        mode = nums[0]

        # Find a mode candidate
        for num in nums:
            if vote == 0:
                mode = num
            
            if num == mode:
                vote += 1
            else:
                vote -= 1
        
        # Verify if it is really the mode
        count = 0
        for num in nums:
            if num == mode:
                count += 1
        
        if count > len(nums) // 2:
            return mode
        else:
            return 0
            