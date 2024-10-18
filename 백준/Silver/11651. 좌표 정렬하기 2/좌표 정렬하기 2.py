import sys

n = int(sys.stdin.readline())
list1=[]

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    list1.append(a)



list1.sort(key = lambda x : (x[1],x[0]))

for a,b in list1:
    print("{} {}".format(a,b))