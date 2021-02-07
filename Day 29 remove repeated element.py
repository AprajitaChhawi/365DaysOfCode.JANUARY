try:
    t=int(input())
    while t:
        t=t-1
        l=input()
        k=[]
        k.append(l[0])
        for i in range(1,len(l)):
            if(k[-1]!=l[i]):
                k.append(l[i])
        for i in k:
            print(i,end="")
        print()    
except Exception:
    pass;
