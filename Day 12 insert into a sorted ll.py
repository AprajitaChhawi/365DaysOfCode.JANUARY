#User function Template for python3

def sortedInsert(head1,key):
    newnode=Node(key)
    if head1==None:
        head1=newNode
        return head1
    else:
        curr=head1
        prev=None
        while(curr and curr.data<key):
            prev=curr
            curr=curr.next
        if(prev==None):
            next=head1.next
            newnode.next=head1
            head1=newnode
        else:
            newnode.next=prev.next
            prev.next=newnode
        return head1
            
    # code here
    # return head of edited linked list




#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.prev=self.head
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.prev = self.head
        else:
            self.prev.next = new_node
            self.prev = self.prev.next

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        a = LinkedList()
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
        
        key=int(input())
        h=sortedInsert(a.head,key)
        printList(h)

# } Driver Code Ends
