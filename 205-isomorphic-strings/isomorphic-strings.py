class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        myl = {}
        myr = {}
        for i, j in zip(s, t):
            if (i in myl and myl[i] != j) or (j in myr and myr[j] != i):
                return False
            myl[i] = j
            myr[j] = i
        return True
