# User function Template for python3

def reverseWords(S):
    s=""
    S='.'.join(reversed(S.split(".")))
    return S
    # code here 



#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(reverseWords(s))

# } Driver Code Ends
