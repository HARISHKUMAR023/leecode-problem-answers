```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        s2=""
        for i in word1:
            for j in i:
                s1+=j
        for k in word2:
            for p in k:
                s2+=p
        if s1 == s2:
            return True
        else:
            return False