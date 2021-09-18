def sol(score):
    answer = ''
    avg = []
    for i in range(len(score)):
        std = []
        for j in range(len(score[0])):
            std.append(score[j][i])
        std.sort()
        compare = std.pop(std.index(score[i][i]))
        if compare < min(std) or compare > max(std):
            avg.append(sum(std) / len(std))
        else:
            avg.append((sum(std) + compare) / (len(std) + 1))

    for grade in avg:
        if grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer = answer + 'B'
        elif grade >= 70:
            answer = answer + 'C'
        elif grade >= 50:
            answer = answer + 'D'
        else:
            answer = answer + 'F'

    return answer


def solution(scores):
    # 다시 풀어보기
    pass


if __name__ == '__main__':
    input_ = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67],
              [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]
    print(sol(input_))
