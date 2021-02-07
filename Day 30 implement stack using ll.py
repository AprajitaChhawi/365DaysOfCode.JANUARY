# Class to represent a node
'''class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    # The method push to push element into
    # the stack
    def push(self, data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        return

        # Add code here

        # The method pop which return the element
        # poped out of the stack

    def pop(self):
        if(self.head==None):
            return -1
        else:
            temp=self.head
            self.head=self.head.next
            popped=temp.data
            return popped

        # Add code here




#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = Stack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends
