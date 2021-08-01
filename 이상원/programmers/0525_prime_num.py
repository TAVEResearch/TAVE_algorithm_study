import itertools
from typing import List
# https://programmers.co.kr/learn/courses/30/lessons/12977

# TODO: 코드 간단히 하기
def solution(nums: List):
    answer = 0

    group = list(itertools.combinations(nums, 3))  # 함수를 사용해서 3개 그룹을 만듬
    for i in group:
        hap = sum(i)  # 각 그룹의 합
        div = list(i + 1 for i in range(1, hap // 2))  # 1부터 소수 판별할 수 / 2 까지 숫자 리스트 생성
        iteration = 0
        for j in div:  # div를 돌면서
            remain = hap % j  # 나머지 계산
            div[iteration] = 0 if remain != 0 else 1
            iteration += 1  # iteration
        if sum(div) == 0:  # 새로 생성된 리스트 합이 0인 그룹이 존재하면 answer +1
            answer += 1

    return answer


if __name__ == '__main__':
    nums = [1, 2, 7, 6, 4]
    print(solution(nums))
