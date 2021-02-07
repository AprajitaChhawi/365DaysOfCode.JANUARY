#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteMid(head):
    first_po=head
    sec_po=head
    if(head==None or head.next==None):
        return head
    if(head.next.next==None):
        head.next=None
        return head
    while(first_po and first_po.next):
        first_po=first_po.next.next
        sec_po=sec_po.next
    sec_po.data=sec_po.next.data
    sec_po.next=sec_po.next.next
    return head
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    
    #code here




#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n=int(input())
        arr1 = [int(x) for x in input().split()]
        ll = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll.insert(nodeData, tail)

        res=deleteMid(ll.head)
        printList(res)
# } Driver Code Ends
