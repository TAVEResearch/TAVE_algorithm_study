# https://programmers.co.kr/learn/courses/30/lessons/42889
import collections


# TODO: 코드 간단하게 만들기
def solution(N: int, stages: list):
    answer = []
    challenger = len(stages)  # 참여자 수
    notClear = [0] * (N + 1)  # 실패한 사람 수를 담을 리스트
    j = 0

    for i in stages:
        notClear[i - 1] += 1  # 차례로 실패한 사람수 넣기
    for i in notClear:
        fail = 0 if challenger == 0 else i / challenger
        challenger -= i
        notClear[j] = [j + 1, fail]  # 실패율과 번호를 리스트로 입력
        j += 1
    for i in sorted(notClear, key=lambda x: x[1],
                    reverse=True):  # sorted를 사용, reverse로 정렬
        if i[0] > N:  # 문제 번호가 N보다 크면 pass
            continue
        else:
            answer.append(i[0])  # 문제 번호 순서대로 입력
    return answer


import operator


def solution_ju(N, stages):
    print(stages)
    stages.sort()
    print(stages)
    failper = {}
    answer = []

    for i in range(N):
        check = stages[0]
        print(f'check:{check}')
        fail = stages.count(check)
        if (check > N):
            failper[check - 1] = 0
        else:
            failper[check] = fail / len(stages)

        for k in range(fail):
            del stages[0]

        # stages에 없는 경우에 인덱스 에러가 뜨지 않게 하기 위해 break
        if (not stages):
            break

    # stages에 없는 스테이지 실패율 집어 넣기
    for i in range(1, N):
        if i not in failper.keys():
            failper[i] = 0

    sfailper = dict(sorted(failper.items(), key=operator.itemgetter(1), reverse=True))
    # 딕셔너리 value를 기준으로 내림차순 정렬

    for i in range(len(failper)):
        result = list(sfailper.keys())

    return result


if __name__ == '__main__':
    N = 9
    stages = [2, 2, 1, 5, 6, 8, 7, 4, 5, 6, 10]
    print(solution(N, stages))
    print(solution_ju(N, stages))
