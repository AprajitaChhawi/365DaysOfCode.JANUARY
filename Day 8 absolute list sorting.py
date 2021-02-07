#User function Template for python3

def sortList(head):
    curr=head.next
    prev=head
    while(curr):
        if(curr.data<0):
            prev.next=curr.next
            curr.next=head
            head=curr
            curr=prev
        else:
            prev=curr
        curr=curr.next
    '''
    head: head of linkedList
    
    Your method shouldn't print anything
    it should transform the passed linked list
    '''



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
        

    
def PrintList(head):
    while head:
        print(head.data,end=' ')
        head=head.next


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        
        n=int(input())
        ll = LinkedList() # create a new linked list 'll1'.
        nodes_ll = list(map(int, input().strip().split()))
        for nodes in nodes_ll:
            ll.append(nodes)  # add to the end of the list
        
        sortList(ll.head)
        PrintList(ll.head)
        print()


# } Driver Code Ends
