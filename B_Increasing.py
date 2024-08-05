for _ in range(int(input())):
    n=int(input())
    a=sorted(list(map(int,input().split())))
    ans=0
    for i in range(n-1):
        if a[i]==a[i+1]:
            ans+=1
    if ans>0:
        print("NO")
    else:
        print("YES")