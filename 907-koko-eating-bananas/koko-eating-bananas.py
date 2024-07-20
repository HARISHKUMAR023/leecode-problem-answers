class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findMax(v):
            maxi = float('-inf')
            n = len(v)
            # Find the maximum
            for i in range(n):
                maxi = max(maxi, piles[i])
            return maxi
        def call(piles,hourly):
              totalH = 0
              n = len(piles)
                # Find total hours
              for i in range(n):
                    totalH += math.ceil(piles[i] / hourly)
              return totalH
        low = 1
        high = findMax(piles)
        while low <= high:
            mid = (low + high) // 2
            totalH = call(piles, mid)
            if totalH <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
        