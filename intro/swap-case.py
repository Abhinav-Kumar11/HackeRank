def swap_case(s):
    st=str()
    for a in s:
        if a.isupper():
            st+=a.lower()
        elif a.islower():
            st+=a.upper()    
        else:
            st+=a
    return st

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)