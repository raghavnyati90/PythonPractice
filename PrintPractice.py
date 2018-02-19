def print_xxx(n):
    return print(*range(1, n+1), sep='')


def print_combinations(str_input):
    # input in format "HACK 2"
    from itertools import combinations
    s, n = str_input.split()
    for i in range(1, int(n)+1):
        for j in combinations(sorted(s), i):
            print(''.join(j))


def print_combinations_with_replacement(str_input):
    # input in format "HACK 2"
    from itertools import combinations_with_replacement
    s, n = str_input.split()
    for i in combinations_with_replacement(sorted(s), int(n)):
        print(''.join(i))


if __name__ == '__main__':
    number = int(input())
    for x in range(1, number+1):
        print(x, end="", flush=True)
