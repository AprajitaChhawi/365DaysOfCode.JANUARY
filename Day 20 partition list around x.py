# your task is to complete this function
# function should return head after patition list
def partitionlist(head,x):
    curr=head
    lesser=lesserhead=Node(0)
    greater=greaterhead=Node(0)
    while(curr):
        if curr.data<x:
            lesser.next=curr
            lesser=lesser.next
        else:
            greater.next=curr
            greater=greater.next
        curr=curr.next
        greater.next=None
        lesser.next=greaterhead.next
        return lesserhead.next
    # Code here



#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        if(isLengthEvenOrOdd(head)):
            print('Even')
        else:
            print('Odd')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
