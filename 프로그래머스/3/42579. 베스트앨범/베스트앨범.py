from collections import defaultdict

def solution(genres, plays):
    
    
    # 장르별 총 수록개수를 기록한다.
    # d = {'classic': 1450, 'pop': 3100})
    d = defaultdict(int)
    for genre, play in zip(genres, plays):
        d[genre] += play
        
        
    # 수록곡이 많은 장르로 정렬한다.
    [('pop', 3100), ('classic', 1450)]
    new_genre = [(key, val) for key, val in d.items()]
    new_genre.sort(key = lambda x : -x[1])
    
    
    # (고유번호, 재생횟수로 hash에 넣어준다.)
    d = dict()
    cnt = 0
    for genre, play in zip(genres, plays):
        if genre in d:
            d[genre].append((cnt, play))
        else:
            d[genre] = []
            d[genre].append((cnt, play))
        cnt += 1
        
        
    # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
    #  장르별로 두개씩 조건에 맞도록 정렬하여 ans 에 넣어준다.
    answer = []
    for x in new_genre:
        genre = x[0]
        
        d[genre].sort(key = lambda x : (-x[1], x[0]))
        
        if len(d[genre]) >= 2:
            answer.append(d[genre][0][0])
            answer.append(d[genre][1][0])
        else:
            answer.append(d[genre][0][0])
    
    
    return answer