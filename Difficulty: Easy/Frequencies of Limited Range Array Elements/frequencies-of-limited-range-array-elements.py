class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # code here
        my={}
        for i in range(1, len(arr) + 1):
            my[i] = 0

        # Count occurrences of each index in arr
        for i in range(len(arr)):
            if arr[i] in my:
                my[arr[i]] += 1
        # print(my)
        c=0
        for j ,k in my.items():
            # print(j,k)
            arr[c]=k
            c+=1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends