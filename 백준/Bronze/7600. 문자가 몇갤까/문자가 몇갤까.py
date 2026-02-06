import sys

input = sys.stdin.readline


def main():
    while True:
        line = input().strip()

        if line == '#':
            break

        alphabets = set()

        for ch in line.lower():
            if 'a' <= ch <= 'z':
                alphabets.add(ch)

        print(len(alphabets))


if __name__ == "__main__":
    main()
