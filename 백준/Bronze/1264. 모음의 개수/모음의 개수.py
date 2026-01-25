import sys

input = sys.stdin.readline


# 변수 및 입력 선언

def main():
    while True:
        line = sys.stdin.readline().rstrip()
        if line == "#":
            break

        count = 0
        for ch in line:
            if ch in 'aeiouAEIOU':
                count += 1

        print(count)


if __name__ == "__main__":
    main()
