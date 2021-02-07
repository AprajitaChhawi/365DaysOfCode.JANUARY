def reverse(A):
    if(A<0):
        A=abs(A)
        A1=''.join(reversed(str(A)))
        return -int(A1)
    else:
        A1=''.join(reversed(str(A)))
        return int(A1)
print(reverse(-123))
