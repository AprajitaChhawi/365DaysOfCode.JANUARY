# your task is to complete this function
# function should return the sum of the nodes of the linked list
def sumofnodes(head):
    curr=head
    s=0
    while(curr):
        s=s+curr.data
        curr=curr.next
    return s
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
        k=sumofnodes(head)
        print(k)
        
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
