class Solution:
    def reverse(self, x: int) -> int:
            
            INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
            rev = 0
            sign = -1 if x < 0 else 1  # Check if the number is negative
            x = abs(x)  # Work with the absolute value
            
            while x != 0:
                l = x % 10
                rev = rev * 10 + l
                x //= 10
            
            rev *= sign  # Restore the sign
            
            # Check for overflow
            if rev < INT_MIN or rev > INT_MAX:
                return 0
            
            return rev
            