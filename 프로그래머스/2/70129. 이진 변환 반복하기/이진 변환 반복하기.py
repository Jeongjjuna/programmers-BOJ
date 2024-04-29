def solution(s):

    binary_count = 0
    zero_remove_count = 0
    
    while s != "1":
        one_count = count_one(s)
        zero_remove_count += len(s) - one_count
        
        s = convert_to_bin(one_count)
        binary_count += 1
    
    answer = [binary_count, zero_remove_count]
    return answer

# 1의 개수를 카운트한다.
def count_one(s):
    cnt = 0
    for elem in s:
        if elem == "1":
            cnt += 1
    return cnt


# 정수 4 -> 문자열 2진수 "100"
def convert_to_bin(number):
    return str(bin(number)[2:])
