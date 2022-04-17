class Solution:
    def hammingWeight(self, n: int) -> int:
        """Determine if LSB is 1 and then right shift."""
        count = 0

        while n:
            # n & 1 == 1 => LSB is 1
            # n & 1 == 0 => LSB is 0
            if n & 1 == 1:
                count += 1
            # Right shift by 1
            n >>= 1
        
        return count
