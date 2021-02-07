#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def modularNode(head, k):
    curr=head
    temp=0
    i=0
    while(curr):
        i=i+1
        if(i%k==0):
            temp=curr.data
        curr=curr.next
    if(k>i):
        return -1
    return temp

    #function should return the modular Node
    #if no such node is present then return -1




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
        
 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        k=int(input())
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(modularNode(a.head,k))


# } Driver Code Ends
