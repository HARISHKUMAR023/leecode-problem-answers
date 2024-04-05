``` python 

#crateing node in Linkded List
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

#creating new node and inserting new value in node 
node1 = Node('harish')
head = node1
node2 = Node('siva')
node3 = Node('sivadharshan')
node4 = Node('barathi')
node5 = Node('lakshmi')

#connnecting each node each other
node1.next = node2
node2.next= node3
node3.next = node4
node4.next = node5

pointer = head 
# inserting new node in beggning of the Linkded list 
newnode = Node('i am new node ')
newnode.next = head 
head = newnode 

#inserting new node in end og the linkded list 
nodeend = Node('new node end')
pointer = head 
while(pointer.next != None):
    pointer = pointer.next
pointer.next = nodeend
pointer= head


#inseting new node after the in middel of some node 
after = 'siva'
nodeMiddel = Node('i am value in middel of the node')

pointer = head 
while(pointer):
    if (pointer.value == after):
        nodeMiddel.next = pointer 
        pointer.next = nodeMiddel
        break 
    else:
        pointer = pointer.next

pointer =  head 




#printing the all data in linkedlist 
while(pointer != None):
    print(pointer.data)
    pointer = pointer.next
    
    