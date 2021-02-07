t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    prod=1
    while(k!=0):
        k=k-1
        temp=min(l)
        print(temp)
        prod=prod*temp
        l.remove(temp)
    print(prod%(10**9+7))
