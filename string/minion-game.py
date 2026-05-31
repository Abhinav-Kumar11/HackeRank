def minion_game(string):
    v='aeiouAEIOU'
    cs=ck=0
    n=len(string)
    for a in range(len(string)):
        if(string[a] in v):
            ck+=n-a
        else:
            cs+=n-a
    if(ck>cs):print("Kevin",ck)
    elif(ck<cs):print("Stuart",cs)
    else:print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)