def duplicates(arr, n):
    dic={}
    l=[]
    for x in arr:
        if x in dic:
            dic[x]=dic[x]+1
        else:
            dic[x]=1
    for i in dic:
        if dic[i]>1:
            l.append(i)
    if(len(l)==0):
        return [-1]
    else:
        l.sort()
        return l
                
        
	# code here
	    



#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
