def is_leap(year):
    return (year % 4 == 0) and ((year % 400 == 0) or (year % 100 != 0))


def compress_string(str_input):
    """
    You are given a string.
    Suppose a character '' occurs consecutively  times in the string.
    Replace these consecutive occurrences of the character '' with  in the string.
    """
    from itertools import groupby
    print(*[(len(list(c)), int(k)) for k, c in groupby(str_input)])


