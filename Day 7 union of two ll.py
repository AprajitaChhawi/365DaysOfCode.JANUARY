#User function Template for python3

def union(head1,head2):
    l1=[]
    l2=[]
    while(head1):
        l1.append(head1.data)
        head1=head1.next
    while(head2):
        l2.append(head2.data)
        head2=head2.next
    l3=sorted(set(l1).union(set(l2)))
    ll3=linkedList()
    for i in l3:
        ll3.insert(i)
    return ll3.head
    # code here
    # return head of resultant linkedlist





#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    for _ in range(int(input())):
        
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        printList(union(ll1.head,ll2.head))
        print()

# } Driver Code Ends
