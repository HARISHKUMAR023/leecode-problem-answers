``` python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        mys=s.split()
        return len(mys[-1])