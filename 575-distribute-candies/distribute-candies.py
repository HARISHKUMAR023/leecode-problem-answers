class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        my={}
        for i in candyType:
            my[i]=my.get(i,0)+1
        if int(len(candyType) / 2) == len(my):
            return len(my)
        elif int(len(candyType) / 2) < len(my):
            return int(len(candyType) / 2)
        else:
            return len(my)