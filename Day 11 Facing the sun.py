#User function Template for python3
class Solution:
    
    def countBuildings(self,h, n):
        count=1
        for i in range(1,n):
            if h[i] < h[i-1] :
                h[i] =h[i-1]
        return len(set(h))
        
        # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        h = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countBuildings(h, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
