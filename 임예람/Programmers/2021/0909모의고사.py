def solution(answers):
    #수포자들의 찍기 답지
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []
    
    #정답지와 수포자들의 찍기 답지와 비교해서 점수 매기기
    for idx, answer in enumerate(answers):
        if answer == a1[idx % 5]:
            score[0] += 1
        if answer == a2[idx % 8]:
            score[1] += 1
        if answer == a3[idx % 10]:
            score[2] += 1
            
    #가장 높은 점수를 가진 사람을 결과 리스트에 넣기
    for idx, grade in enumerate(score):
        if grade == max(score):
            result.append(idx + 1)
    
    return result