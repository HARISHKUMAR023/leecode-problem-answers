#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
        def factorial(x):
            if x == 0 or x == 1:
                return 1
            else:
                return x * factorial(x - 1)

        result = []
        i = 1
        while True:
            fact = factorial(i)
            if fact > n:
                break
            result.append(fact)
            i += 1

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends