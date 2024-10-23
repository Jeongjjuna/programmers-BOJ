n = int(input())

answer = []

def star(n):
    global answer

    if n == 3:
        answer.append(['*','*','*'])
        answer.append(['*',' ','*'])
        answer.append(['*','*','*'])
        return
    
    star(n//3)


    for i in range(n//3):
        answer.append(answer[i] + [' ']*(n//3) + answer[i])

    for i in range(n//3):
        answer.append(answer[i]*3)

    for i in range(n//3):
        answer[i] = answer[i]*3



star(n)

for i in range(n):
    print("".join(answer[i]))