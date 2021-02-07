#User function Template for python3
'''Your task is to check given two strings
   are anagrams or not.
   a,b: given strings
   
   Return True or False accordingly.
   
   -> You don't need to print anything.Return type of function
   is boolean.
'''

def isAnagram(a,b):
    if(len(a)!=len(b)):
        return False
    a1=sorted(a)
    b1=sorted(b)
    if(a1==b1):
        return True
    else:
        return False
    #code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends
