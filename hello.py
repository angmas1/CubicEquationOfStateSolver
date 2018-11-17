import sys

print("Enter number")
n=sys.stdin.readline()
n=int(n)
a=[-1]
for i in range(1,n+1):
    a.append(-1)

def total(x):
    f=int(x/2)
    g=int(x/3)
    h=int(x/4)
    print(f,g,h)
    if(f==0):
        print(f)
    elif(a[f]!=-1):
        f=a[f]
        print("f")
    else:
        f=total(f)

    if(g==0):
        print(g)
    elif (a[g] != -1):
        g = a[g]
        print("g")
    else:
        g = total(g)


    if(h==0):
        print(h)
    elif (a[h] != -1):
        h = a[h]
        print("h")
    else:
        h = total(h)

    if((f+g+h)<=x):
        return x
    else:
        x = f + g + h
        return x


print(total(n))