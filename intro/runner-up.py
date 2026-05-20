if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    srt=sorted(arr,reverse=True)
    for a in range(n):
        if(srt[0]>srt[a]):
            print(srt[a])
            break