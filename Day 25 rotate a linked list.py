# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

# This function should rotate list counter-
# clockwise by k and return head node
def rotate(head, k):
    curr=head
    count=0
    prev=None
    next=None
    while(count!=k):
        count=count+1
        prev=curr
        curr=curr.next
    if(curr==None):
        prev.next=next
        return head
    next=head
    head=curr
    prev.next=None
    if(curr):
        while(curr and curr.next):
            curr=curr.next
        curr.next=next
    return head
    
    # code here




#{ 
#  Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = rotate(lis.head,k)
        printList(head)
# } Driver Code Ends
