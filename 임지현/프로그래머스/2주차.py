def solution(scores):
    answer = ''
    for i in range(len(scores)):
        tmp = []
        for j in range(len(scores)):
            tmp.append(scores[j][i])
        if max(tmp) == tmp[i] and tmp.count(tmp[i]) == 1:
            del tmp[i]
        elif min(tmp) == tmp[i] and tmp.count(tmp[i]) == 1:
            del tmp[i]
        avg = sum(tmp)/len(tmp)
        rating = get_rating(avg)
        answer += rating

    return answer

def get_rating(avg):
    if avg >= 90:
        return 'A'
    elif 80 <= avg < 90:
        return 'B'
    elif 70 <= avg < 80:
        return 'C'
    elif 50 <= avg < 70:
        return 'D'
    else:
        return 'F'
