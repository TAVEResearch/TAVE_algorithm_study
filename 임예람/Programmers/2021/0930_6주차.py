#입력 
# 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
# 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
# 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
# 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.
weights = [60,70,60]	
head2head = ["NNN","NNN","NNN"]
#출력 [3,4,1,2]
#점수 67점..ㅜㅜㅜㅜ

import math
def solution(weights, head2head):
    answer = []
    player =[] #ex)[[1, 50, 'NLWL'], [1, 82, 'WNLL'],...]
    #선수들을 인덱스별로 dic에 무게와 전적을 저장한다.
    for num in range(len(weights)):
        player.append([num+1, weights[num], head2head[num]])

    #player에 각 복서들의 부가 내용 추가한다. ex) [[1, 50, 'NLWL', 33.33, 1],...]
    for idx1, value1 in enumerate(player): #record=[1, 50, 'NLWL']
        if 'W' not in value1[2]:#이긴적이 없으면 승률=0
            value1.append(0.0) 
            value1.append(0) 
        else:#이긴 적이 있다면 승률추가
            value1.append(math.trunc(value1[2].count('W') / (int(len(value1[2]) - int(value1[2].count('N')))) * 10000) /100)
            heavy_win = 0
            #본인보다 무거운 사람 이긴 횟수 추가
            for idx2, value2 in enumerate(player):
                if idx2 == idx1:#본인 제외
                    continue
                else: 
                    if value2[1] > value1[1]:#본인보다 무거운 사람을 이겼는가
                        if value1[2][idx2] == 'W':
                            heavy_win += 1
                    else:
                        continue
            value1.append(heavy_win)

    #조건에 맞게 정렬하고 번호를 입력
    sorted_player = sorted(player, key=lambda x : (-x[3], -x[4], -x[1], x[0]))
    for i in sorted_player:
        answer.append(i[0])

    return answer

print(solution(weights, head2head))