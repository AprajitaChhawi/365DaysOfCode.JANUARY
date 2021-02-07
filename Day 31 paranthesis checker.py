#User function Template for python3
'''
Function Arguments :
		@param  : s (given string containing parenthesis) 
		@return : boolean True or False
'''
def isEqual(a,b):
    if(str(a)==')' and str(b)=='('):
        return True
    elif(str(a)=='}' and str(b)=='{'):
        return True
    elif(str(a)==']' and str(b)=='['):
        return True
    else:
        return False
def ispar(x):
    l=[]
    for i in x:
        if(str(i)=='[' or str(i)=='(' or str(i)=='{'):
            l.append(i)
        if(str(i)==']' or str(i)==')' or str(i)=='}'):
            if(len(l)==0):
                return False
            temp=l[-1]
            k=isEqual(i,temp)
            if k==False:
                return False
            l.pop()
    if(len(l)==0):
        return True
    else:
        return False
    # code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends
