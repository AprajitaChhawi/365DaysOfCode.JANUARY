#User function Template for python3

class Solution:
    def sumOfDigits (self, N):
        l1=map(int,list(str(N)))
        return sum(l1)
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends
