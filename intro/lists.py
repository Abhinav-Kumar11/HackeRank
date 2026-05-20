if __name__ == '__main__':
    lst=[]
    N = int(input())
    for a in range(N):
        d=input().split()
        if(d[0]=='insert'):
            lst.insert(int(d[1]),int(d[2]))
        elif(d[0]=='print'):
            print(lst)
        elif(d[0]=='remove'):
            lst.remove(int(d[1]))
        elif(d[0]=='append'):
            lst.append(int(d[1]))
        elif(d[0]=='sort'):
            lst.sort()
        elif(d[0]=='pop'):
            lst.pop()
        else:
            lst.reverse()