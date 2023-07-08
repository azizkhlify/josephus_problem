def sous(c,n):
    if n>=len(c)-1:return [c[1:],n-(len(c)-1)]
    return [c[:n+1]+c[n+2:],n+1]
def jos(c,n):
    if len(c)==1:return c[0]
    elif 0<=n<=len(c)-1 :
        x=sous(c,n)
        return jos(x[0],x[1])
    else :
        n%=(len(c))
        return jos(c,n)
def remplir(n):
    c=[]
    for i in range(n):
        c.append(i+1)
    return c
n=int(input())
t=remplir(n)
print(jos(t,0))
