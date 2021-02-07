def isPalindrome(A):
    A1=''.join(reversed(str(A)))
    print(A1)
    print(A)
    if(int(A1)==A):
        return True
    else:
        return False
print(isPalindrome(121))
