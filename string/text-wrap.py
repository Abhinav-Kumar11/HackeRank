import textwrap
def wrap(string, max_width):
    cnt=1
    s=str()
    for a in string:
        if(cnt%max_width==0):
            s+=a
            s+='\n'
        else:
            s+=a
        cnt+=1
    return s
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)