# 모의고사

def solution(answers: list) -> list:
    answer = []
    std = [0] * 3
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one = one * (len(answers) // len(one)) + one[:len(answers) % len(one)]
    two = two * (len(answers) // len(two)) + two[:len(answers) % len(two)]
    three = three * (len(answers) // len(three)) + three[:len(answers) % len(three)]

    for i in range(len(answers)):
        if answers[i] == one[i]:
            std[0] += 1
        if answers[i] == two[i]:
            std[1] += 1
        if answers[i] == three[i]:
            std[2] += 1
    top = max(std)
    for i in range(len(std)):
        if std[i] == top:
            answer.append(i + 1)

    return answer


# 주희
def solution_j(answers):
    cor = [0] * 3

    result = []
    stu = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for count, ans in enumerate(answers):
        if ans == stu[count % 5]:
            cor[0] += 1
        if ans == stu2[count % 8]:
            cor[1] += 1
        if ans == stu3[count % 10]:
            cor[2] += 1
    high = max(cor)
    for count, ans in enumerate(cor):
        if ans == high:
            result.append(count + 1)
    return result


# 인규
def solution_i(answers: list) -> list:
    result = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0 for _ in range(3)]
    for i, answer in enumerate(answers):
        if answer == num1[i % len(num1)]:
            score[0] += 1
        if answer == num2[i % len(num2)]:
            score[1] += 1
        if answer == num3[i % len(num3)]:
            score[2] += 1
    for i, s in enumerate(score):
        if s == max(score):
            result.append(i + 1)
    return result


inp_ = [1, 2, 3, 4, 5]
print(solution_j(inp_))
