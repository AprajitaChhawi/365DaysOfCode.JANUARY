# your task is to complete this function
# function should return an integer
def atoi(string):
    s=""
    k=0
    if(ord(string[0])==45):
            s+=string[0]
            k=k+1
    for i in range(k,len(string)):
        if(ord(string[i])<48 or ord(string[i])>57):
            return -1
        else:
            s+=string[i]
    return s
    # Code here



#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        print(atoi(string))
# Contirbuted By: Harshit Sidhwa
# } Driver Code Ends
