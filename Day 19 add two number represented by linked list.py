#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

def addTwoLists(first, second):
    if(first==None):
        return second
    if(second==None):
        return first
    len1=0
    len2=0
    next1=None
    prev1=None
    curr1=first
    while(curr1):
        len1=len1+1
        next1=curr1.next
        curr1.next=prev1
        prev1=curr1
        curr1=next1
    first=prev1
    next2=None
    prev2=None
    curr2=second
    while(curr2):
        len2=len2+1
        next2=curr2.next
        curr2.next=prev2
        prev2=curr2
        curr2=next2
    second=prev2
    if(len1>=len2):
        longer=first
        shorter=second
    else:
        longer=second
        shorter=first
    s=None
    carry=0
    while shorter!=None:
        value=shorter.data+longer.data+carry
        carry=int(value/10)
        value=value%10
        if s==None:
            s=Node(value)
            result=s
        else:
            s.next=Node(value)
            s=s.next
        shorter=shorter.next
        longer=longer.next
    while longer!=None:
        value=longer.data+carry
        carry=int(value/10)
        value=value%10
        s.next=Node(value)
        s=s.next 
        longer=longer.next
    if(carry!=0):
        s.next=Node(carry)
    next3=None
    prev3=None
    curr3=result
    while(curr3):
        next3=curr3.next
        curr3.next=prev3
        prev3=curr3
        curr3=next3
    return prev3
        
    # code here
    # return head of sum list



#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends
