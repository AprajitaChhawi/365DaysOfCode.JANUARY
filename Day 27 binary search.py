#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
	    low=0
	    high=len(arr)-1
	    mid=0
	    while(low<=high):
	        if(arr[mid]==k):
	            return mid
	        elif(arr[mid]>k):
	            high=mid-1
	        elif(arr[mid]<k):
	            low=mid+1
	    return -1
		# code here







#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends
