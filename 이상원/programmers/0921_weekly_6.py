import collections


def solution(weights, head2head):
    total = []
    answer = []
    self = 1000
    _index = 0

    for _iter in head2head:
        score = 0
        win = 0
        lose = 0
        ratio = 0
        for _idx in range(len(weights)):
            bx = _iter[_idx]
            kg = weights[_idx]
            self = weights[_index]
            if bx == 'W' and self < kg:
                score += 1
                win += 1
            elif bx == 'W':
                win += 1
            elif bx == 'L':
                lose += 1
            if win + lose != 0:
                ratio = win / (win + lose) * 100
            else:
                ratio = 0
        _index += 1
        total.append([_index, self, score, ratio])
    total.sort(key=lambda x: (x[3], x[2], x[1]), reverse=True)
    for tot in total:
        answer.append(tot[0])
    return answer


if __name__ == '__main__':
    weights = [50, 82, 75, 120]
    head2head = ["NLWL", "WNLL", "LWNW", "WWLN"]
    print(solution(weights, head2head))
