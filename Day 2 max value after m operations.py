try:
    t=int(input())
    while t:
        t=t-1
        n,m=map(int,input().split())
        l=[0]*n
        while m:
            m=m-1
            l1=list(map(int,input().split()))
            for h in range(0,len(l1)-2,3):
                a=l1[h]
                b=l1[h+1]
                k=l1[h+2]
                for i in range(a,b+1,1):
                    l[i]=l[i]+k
        print(max(l))
except Exception:
    pass;
