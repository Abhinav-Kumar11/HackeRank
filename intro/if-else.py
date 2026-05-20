if __name__ == '__main__':
    n = int(input().strip())
    if (n%2!=0):
        print("Weird")
    else:
        if ((n>1 and n<6) or n>20):
            print("Not Weird")
        else:
            print("Weird")