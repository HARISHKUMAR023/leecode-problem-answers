class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n + 1)
        # print(prefix)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        result = []
        for L, R in queries:
            result.append(prefix[R + 1] ^ prefix[L])
        
        return result
        # print(prefix)
        # ans=[]
        # for i in queries:
        #     a=0
        #     for j in arr[i[0]: i[1]+1]:
        #          a^=j
        #     ans.append(a)
        #     a=0
        # return ans

        