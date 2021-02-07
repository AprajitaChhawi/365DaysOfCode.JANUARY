'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
# function inserts data x in front of list and returns new head 
def insertAtBegining(head,x):
    newnode=Node(x)
    newnode.next=head
    head=newnode
    return head
    
    # code here 

# function appends data x at the end of list and returns new head
def insertAtEnd(head,x):
    newnode=Node(x)
    if head is None:
        head=newnode
        return head
    temp=head
    while(temp.next):
        temp=temp.next
    temp.next=newnode
    return head
    # code here 





#{ 
#  Driver Code Starts
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
    print()

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a=LinkedList()
        
        nodes_info=list(map(int,input().split()))
        for i in range(0,len(nodes_info)-1,2):
            if(nodes_info[i+1]==0):
                a.head = insertAtBegining(a.head,nodes_info[i])
            else:
                a.head = insertAtEnd(a.head,nodes_info[i])
        printList(a.head)

 
# } Driver Code Ends
