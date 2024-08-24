class Solution:
    def isPalindrome(self, x: int) -> bool:
         l=0
         r=len(str(x))-1
         v=str(x)
         while l<= r:
            if v[l] != v[r]:
                return False
            l+=1
            r-=1
         return True

        # st=str(x)
        # l=len(st)-1
        # d=l
        # sti=""
        # for i in st:
        #     sti+=st[d]
        #     d-=1
        # if st == sti:
        #     return True
        # else:
        #     return False
