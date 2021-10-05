def solution(weights, head2head):
    answer = []
    all_info = []

    for i,v in enumerate(head2head):

        # 자기 몸무게보다 무거운 선수를 이긴 횟수, 대결 횟수
        heavy_cnt = 0
        p_cnt = 0  # 대결 횟수
        for j,lw in enumerate(v):
            if lw == "W" and weights[i] < weights[j]:
                heavy_cnt += 1
            if lw != "N":
                p_cnt += 1

        if p_cnt == 0:
            win_rate = 0
        else:
            win_rate = v.count("W")/p_cnt*100

        all_info.append((win_rate,heavy_cnt, weights[i], i+1))
        # [승률, 자신보다 무거운 선수를 이긴 횟수, 본인 몸무게, 자기 번호]
        # [(33.33333333333333, 1, 50, 1), (33.33333333333333, 0, 82, 2), (66.66666666666666, 2, 75, 3), (66.66666666666666, 0, 120, 4)]

    sorted_val = sorted(all_info, key = lambda x : (-x[0], -x[1], -x[2], x[3]))
    # [(66.66666666666666, 2, 75, 3), (66.66666666666666, 0, 120, 4), (33.33333333333333, 1, 50, 1), (33.33333333333333, 0, 82, 2)]
    
    for tup in sorted_val:
        answer.append(tup[3])

    return answer
    

weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]
print(solution(weights, head2head))
