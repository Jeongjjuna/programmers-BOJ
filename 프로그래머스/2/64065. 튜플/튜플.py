
'''
ex1) elem = '2'        -> {2} 
ex2) elem = '2,1,3,4'  -> {2, 1, 3, 4}
'''
def to_dict(s):
    return set(map(int, s.split(',')))


'''
방법 1. s안의 튜플원소를 집합으로 변환한다. 집합의 뺄셈 이용
아래와 같이 집합의 뺄셈을 이용해보자.
a = {1, 2, 3} - {1, 3} = {2}    
'''
def solution(s):
    
    # 각 요소를 집합의 자료료형으로 만들어준다.
    # [{1,2,3},{2,1},{1,2,4,3},{2}]
    parsed_data = s.split("},{")
    parsed_data[0] = parsed_data[0].strip("{{")
    parsed_data[-1] = parsed_data[-1].strip("}}")
    
    dict_data = [to_dict(elem) for elem in parsed_data]
    
    # 길이 오름차순으로 정렬
    # [{2}, {2,1}, {1,2,3},{1,2,4,3}]
    dict_data.sort(key = lambda x : len(x))
       
    # 뺀값을 answer에 넣기
    
    # first_elem = dict_data[0].pop()
    # answer = [first_elem]
    answer = list(dict_data[0])
    for i in range(len(dict_data) - 1):
        elem = dict_data[i + 1] - dict_data[i]
        answer.append(elem.pop())
        
    return answer