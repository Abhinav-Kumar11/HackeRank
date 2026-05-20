def print_formatted(number):  
    width = len(format(number, 'b'))  # max width

    for a in range(1, number + 1):
        print(
            format(a, f'>{width}'),
            format(a, f'>{width}o'),
            format(a, f'>{width}x').upper(),
            format(a, f'>{width}b')
        )
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)