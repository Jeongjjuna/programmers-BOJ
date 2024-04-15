from functools import cmp_to_key


def compare(x, y):
    if int(x + y) > int(y + x):
        return -1
    if int(x + y) < int(y + x):
        return 1
    return 0



def solution(numbers):
    
    numbers = list(map(str, numbers))
    
    numbers.sort(key = cmp_to_key(compare))
    
    if numbers[0] == "0":
        return "0"
    
    return "".join(numbers)