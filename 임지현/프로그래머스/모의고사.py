def solution(answers):
    num_1 = [1,2,3,4,5]
    num_2 = [2,1,2,3,2,4,2,5]
    num_3 = [3,3,1,1,2,2,4,4,5,5]
    cnt_1, cnt_2, cnt_3 = 0, 0, 0

    for i,answer in enumerate(answers):
        i_1 = i%len(num_1)
        i_2 = i%len(num_2)
        i_3 = i%len(num_3)
        if answer == num_1[i_1]:
            cnt_1 += 1
        if answer == num_2[i_2]:
            cnt_2 += 1
        if answer == num_3[i_3]:
            cnt_3 += 1

    max_cnt = max(cnt_1, cnt_2, cnt_3)
    result = []
    if max_cnt == cnt_1:
        result.append(1)
    if max_cnt == cnt_2:
        result.append(2)
    if max_cnt == cnt_3:
        result.append(3)

    return result
