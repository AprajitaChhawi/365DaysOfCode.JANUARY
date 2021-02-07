#User function Template for python3

'''
	Your task is tocheck if the given two strings
	are rotations of each other.
	Function Arguments: s1 and s2 (given strings)
	Return Type:boolean
'''

def areRotations(s1,s2):
    len1=len(s1)
    len2=len(s2)
    if len1!=len2:
        return False
    temp=s1+s1
    if(temp.count(s2)>0):
        return True
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
        s1=str(input())
        s2=str(input())
        if(areRotations(s1,s2)):
            print(1)
        else:
            print(0)
    
        
# } Driver Code Ends
