class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[i:len(needle)+i]:
                return i
        return -1
