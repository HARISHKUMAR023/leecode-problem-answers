```python
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans=0

        if len(words)==0 or len(words) == 1:
            return 0
        for i in range(0,len(words)-1):
            w=words[i]
            r=w[::-1]
            if i == len(words)-1:
                return ans
            for j in range(i+1,len(words)):
                if r == words[j]:
                    ans+=1
        return ans