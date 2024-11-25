

x = int(input())

if x == 64:
    print(1)
    exit()

stick = 64
sticks = []

while (stick != 1):
    temp = stick // 2
    if (x < temp):
        stick = temp
    else:
        stick = temp
        sticks.append(temp)


sum = 0
cnt = 0
for stick in sticks:
    if (sum + stick > x):
        continue
    elif (sum + stick == x):
        cnt += 1
        break
    else:
        sum += stick
        cnt += 1

print(cnt)