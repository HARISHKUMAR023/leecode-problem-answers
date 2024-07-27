class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        last= self.fib(n-1)
        f=self.fib(n-2)
        return last+f
