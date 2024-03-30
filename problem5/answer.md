``` python
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for i in words:
            fs=0
            for j in i:
                if j in allowed:
                  fs=1
                else:
                    fs=0
                    break
            if  fs == 1:
                c+=1
        return c