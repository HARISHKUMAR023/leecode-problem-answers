class Solution:
    def checkValidString(self, s: str) -> bool:
        min_o=0
        max_o=0
        for i in s:
            if i == '(':
                min_o+=1
                max_o+=1
            elif i ==  ')':
                min_o-=1
                max_o-=1
            else:
                min_o-=1
                max_o+=1
            if min_o < 0:
                min_o = 0
            if max_o <0:
                return False
        return min_o == 0
