class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        r= start^goal
        v=bin(r).count('1')
        return v
        