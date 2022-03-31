#학점 계산기
def eachGrade(avg):
    if avg >= 90:
        return'A'
    elif 90 > avg >= 80:
        return'B'
    elif 80 > avg >= 70:
        return'C'
    elif 70 > avg >= 50:
        return'D'
    else:
        return'F'

def solution(scores):
    avg = []
    grade = ''
    
    #해당 학생이 타 학생에게 준 점수배열을 돌린다.
    for i in range(0, len(scores)):
        recieve_scores = []
        my_score = 0
        
        #타 학생에게 준 점수 배열 속에 점수를 각 학생에게 잘 넣어준다. 
        for j in range(0, len(scores)):
            recieve_scores.append(scores[j][i])
            #해당 학생이 본인에게 준 점수를 적어둔다.
            if j == i:
                my_score = scores[j][i]
            
        #본인에게 준 점수가 최대 or 최소?
        if my_score == max(recieve_scores) or my_score == min(recieve_scores):
            #그 최대or최소가 1개 이상이면 바로 평균 구해서 배열에 저장한다.
            if recieve_scores.count(my_score) > 1:
                avg.append(sum(recieve_scores)/len(recieve_scores))
            #1개이면 제외하고 평균 구한다.
            else:
                avg.append((sum(recieve_scores)-my_score)/(len(recieve_scores)-1))
        #최대or최소 아니면 바로 평균 구한다.
        else:
            avg.append(sum(recieve_scores)/len(recieve_scores))
                
    #학점 계산
    for eachAvg in avg:
        grade += eachGrade(eachAvg)
                
    return grade