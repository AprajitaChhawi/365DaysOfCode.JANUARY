#User function Template for python3

def rearrangeEvenOdd(head):
    starteven=None
    endeven=None
    startodd=None
    endodd=None
    curr=head
    if(head==None or head.next==None):
        return head
    while(curr):
        temp=curr.data
        if(temp%2==0):
            if(starteven==None):
                starteven=curr
                endeven=starteven
            else:
                endeven.next=curr
                endeven=endeven.next
        else:
            if(startodd==None):
                startodd=curr
                endodd=startodd
            else:
                endodd.next=curr
                endodd=endodd.next
        curr=curr.next
    if(starteven==None or startodd==None):
        return head
    else:
        endodd.next=starteven
        head=startodd
        return head
            
            
                
                
    #code here



#{ 
#  Driver Code Starts
# Python3 program to rearrange a linked list 
# in such a way that all odd positioned 
# node are stored before all even positioned nodes 
# Linked List Node 
class Node: 
	def __init__(self, d): 
		self.data = d 
		self.next = None

class LinkedList: 
	def __init__(self): 
		self.head = None
		
	# A utility function to create 
	# a new node 
	def newNode(self, key): 
		temp = Node(key) 
		self.next = None
		return temp 

	# Rearranges given linked list 
	# such that all even positioned 
	# nodes are before odd positioned. 
	# Returns new head of linked List. 
	

	# A utility function to print a linked list 
	def printlist(self, node): 
		while (node != None): 
			print(node.data, end = " ") 
			node = node.next
		
	# Function to insert a new node 
	# at the beginning 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

# Driver code 
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        ll = LinkedList() 
        for i in range(n-1,-1,-1):
            ll.push(a[i])
        start = rearrangeEvenOdd(ll.head) 
        ll.printlist(start) 
        print()

# This code is contributed by Prerna Saini 

# } Driver Code Ends
