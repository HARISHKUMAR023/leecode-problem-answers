class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans = []
        current = 1
        while len(ans) < k:
            if current not in arr:
                ans.append(current)
            current += 1
        return ans[k-1]