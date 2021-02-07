#User function Template for python3


#Complete this function
def convertToWave(a,N):
    for i in range(0,N-1,2):
        a[i],a[i+1]=a[i+1],a[i]
    return a
    #Your code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().split()]
        convertToWave(A,N)
        for i in A:
            print(i,end=" ")
        
        
        print()
        
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
