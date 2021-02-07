#User function Template for python3
import math
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x
class Solution:
    
    def checkFibonacci (ob,N):
        k=isPerfectSquare(5*N*N + 4) or isPerfectSquare(5*N*N - 4)
        if k:
            return "Yes"
        return "No"
            
        # code here 



#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
    
        ob = Solution()
        print(ob.checkFibonacci(N))
# } Driver Code Ends
