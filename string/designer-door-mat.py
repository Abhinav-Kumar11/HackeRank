N,M=map(int,input().split())
for a in range(1,(N+1)//2):
    j=2*a-1
    k=3*j
    l=M-k+j
    for b in range(l):
        if(b<(l-j)//2 or b>(l-j)//2+j-1):
            print("-",end="")
        else:
            print(".|.",end="")
    print()
for a in range(M-6):
    if(a==(M-7)//2):
        print("WELCOME",end="")
    else:
        print("-",end="")
print()
for a in range((N-1)//2,0,-1):
    j=2*a-1
    k=3*j
    l=M-k+j
    for b in range(l):
        if(b<(l-j)//2 or b>(l-j)//2+j-1):
            print("-",end="")
        else:
            print(".|.",end="")
    print()
