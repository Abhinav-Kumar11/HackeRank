if __name__ == '__main__':
    records=[]
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    for a in records:
        if a[1] not in lst:
            lst.append(a[1])
    lst.remove(min(lst))
    mn=min(lst)
    lst.clear()
    for a in records:
        if(a[1]==mn):
            lst.append(a[0])
    records=sorted(lst)
    for a in records:
        print(a)