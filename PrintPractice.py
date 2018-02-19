def print_xxx(n):
    return print(*range(1, n+1), sep='')


if __name__ == '__main__':
    number = int(input())
    for x in range(1, number+1):
        print(x, end="", flush=True)
