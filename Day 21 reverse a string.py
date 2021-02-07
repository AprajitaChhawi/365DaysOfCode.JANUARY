#User function Template for python3

def reverseWord(s):
    s1=""
    for i in range(0,len(s)):
        s1+=s[len(s)-i-1]
    return s1
    #your code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends
