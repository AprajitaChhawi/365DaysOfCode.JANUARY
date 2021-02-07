#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

def addOne(head):
    next=None
    prev=None
    curr=head
    while(curr):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    curr2=head
    carry=0
    curr2.data=curr2.data+1
    while(curr2!=None)and(curr2.data>9 or carry>0):
        prev=curr2
        curr2.data=curr2.data+carry
        carry=int(curr2.data/10)
        curr2.data=curr2.data%10
        curr2=curr2.next
    if(carry!=0):
        prev.next=Node(carry)
    next=None
    prev=None
    curr=head
    while(curr):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head
        
        



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
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends
