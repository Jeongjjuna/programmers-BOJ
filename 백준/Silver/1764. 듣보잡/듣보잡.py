import sys; input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = dict() #듣
    B = dict() #보
    
    for _ in range(N): #O(50만)
        A[input().strip()] = 0

    answer = []
    for _ in range(M): #O(50만)
        hear = input().strip()
        if hear in A:
            answer.append(hear)

    answer.sort() #O(N ln N)
    print(len(answer))
    for word in answer: #O(50만)
        print(word)