# 변수 입력 및 선언
n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

d = dict()
for elem in n_arr:
    d[elem] = 1

for elem in m_arr:
    if elem in d:
        print(1)
    else:
        print(0)