#User function Template for python3




def getFloorAndCeil(arr, n, x):
    # code here
    floor = -1
    ceil = -1
    arr.sort()
    for i in range(n):
        if arr[i] <= x:
            floor = arr[i]
        if arr[i] >= x and ceil == -1:
            ceil = arr[i]
            # We can break the loop as soon as we find the first element greater than or equal to x
            break

    return [floor, ceil]

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends