import sys
input = sys.stdin.readline

# 전공평점 3.3 이상이 되어야함.
# 전공 평점 계산해주기.

score_map = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
    }

subject_sum = 0 
grade_sum = 0
line = 20
for _ in range(line):
    subject_name, score, grade = input().split()
    
    if (grade == "P"):
        continue

    subject_sum += (float(score) * score_map[grade])
    grade_sum += float(score)

print(f"{subject_sum / grade_sum:.6f}")