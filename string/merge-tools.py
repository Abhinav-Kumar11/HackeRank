def merge_the_tools(string, k):
    l=len(string)
    for a in range(l//k):
        word=string[0+a*k:k+a*k]
        s=''
        for b in word:
            if b not in s:
                s+=b
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)