class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        my={}
        a=int(len(candyType) / 2)
        for i in candyType:
            my[i]=my.get(i,0)+1
        if a == len(my):
            return len(my)
        elif a < len(my):
            return int(len(candyType) / 2)
        else:
            return len(my)