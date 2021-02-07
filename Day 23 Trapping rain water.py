#Complete this function
def trappingWater(arr,n):
    l=[0]*n
    r=[0]*n
    l.insert(0,arr[0])
    r.insert(-1,arr[n-1])
    for i in range(1,n):
        l[i]=max(arr[i],l[i-1])
    for i in range(n-2,-1,-1):
        r[i]=max(arr[i],r[i+1])
    sum=0
    for i in range(n):
        sum=sum+(min(l[i],r[i])-arr[i])
    return sum
    #Your code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            print(trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
