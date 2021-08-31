def solution(answers):
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 슬라이딩 윈도우로는 안되나
    def sliding(stdAns: list, answer: list):
        score = 0
        for _iter in range(0, len(answer), len(stdAns)):
            compare = answer[_iter:_iter + len(stdAns)]
            for _ans, _std in zip(compare, stdAns):
                if _ans == _std:
                    score += 1
                else:
                    continue
        return score

    std1Score = sliding(std1, answers)
    std2Score = sliding(std2, answers)
    std3Score = sliding(std3, answers)
    stdList = {1: std1Score, 2: std2Score, 3: std3Score}
    ansout = []
    _max = max(stdList, key=lambda x: stdList[x])

    for i in stdList.items():
        if stdList[_max] == i[1]:
            ansout.append(i[0])

    return ansout


if __name__ == '__main__':
    answer = [1, 2, 3, 4, 5]
    print(solution(answer))
