class Solution:
    def isHappy(self, n: int) -> bool:
        
        my=[]
        if n >= 0:
            ans=n
            while  n  > 1 :
                s=str(n)
                ap=0

                for k in s:
                    ap+=int(k)*int(k)
                n=ap


                if n in my:
                    return False
                    
                else:
                    my.append(n)
            if n == 1:
                return True
            else:
                return False
        else:
            return False
                