import sys

input = sys.stdin.readline

# 변수 및 입력 선언
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split())


def main():
    total_days = 0
    for i in range(x - 1):
        total_days += month_days[i]

    total_days += y
    day_index = total_days % 7
    print(weeks[day_index])


if __name__ == "__main__":
    main()
