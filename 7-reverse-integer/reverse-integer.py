class Solution:
    def reverse(self, x: int) -> int:
            r = ""
            l = ""
            for i in str(x):
                if i == "-":
                    r += i
                else:
                    l += i

            rev = l[::-1]
            f = r + rev
            result = int(f)
            if -2**31 <= result <= 2**31-1:
                return result
            else:
                return 0
        