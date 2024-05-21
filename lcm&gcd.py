#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        a=[0,0] 
        for i in range(1,min(A,B)+1):
             if A % i == 0 and B % i ==0:
                
                 a[1] =i
        l=(A*B)// a[1]
        a[0]=l
        return a
