class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my={}
        for i in strs:
            s = ''.join(sorted(i))
            if s not in my:
                my[s]=[i]
            else:
                my[s].append(i)
        ans=[]
        for j in my.values():
            ans.append(j)
        return ans