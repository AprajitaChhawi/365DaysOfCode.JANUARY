#User function Template for python3

def sumTriangles(matrix, n):
    l1=[]
    sum1=0
    sum2=0
    for i in range(n):
        for j in range(n):
            if(i<=j):
                sum1=sum1+matrix[i][j]
            if(i>=j):
                sum2=sum2+matrix[i][j]
    l1.append(sum1)
    l1.append(sum2)
    return l1
    
            
            
    # code here 



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]

        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
       
        ans = sumTriangles(matrix, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends
