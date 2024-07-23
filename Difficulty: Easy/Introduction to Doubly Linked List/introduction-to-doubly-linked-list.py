#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        if not arr:
            return arr
        head = Node(arr[0])
        c=head
        for i in arr[1:]:
            new_node= Node(i)
            c.next = new_node
            new_node.prev = c
            c=new_node
        return head
            
        

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
    
def printList(node):
    tmp = node
    if tmp:
        c1, c2 = 0, 0
        while tmp.next:
            c1 += 1
            tmp = tmp.next
        while tmp.prev:
            c2 += 1
            tmp = tmp.prev
        if c1 != c2:
            print("-1")
            return
    while tmp:
        print(tmp.data, end = " ")
        tmp = tmp.next
    print()

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructDLL(arr)
        printList(res)
# } Driver Code Ends