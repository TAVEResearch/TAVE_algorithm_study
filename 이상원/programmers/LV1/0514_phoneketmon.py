import collections
import itertools


# 시간 초과
def solution_my(nums):
    answer = 0
    get_num = len(nums) // 2
    list_get = list(itertools.combinations(nums, get_num))
    for i in list_get:
        rem_dupl = set(i)
        if answer < len(rem_dupl):
            answer = len(rem_dupl)
    return answer


def solution(nums):
    answer = 0
    get_num = len(nums) // 2
    num_set = set(nums)
    if get_num > len(num_set):
        answer = len(num_set)
    elif get_num < len(num_set):
        answer = get_num
    else:
        answer = get_num
    return answer


# 갯수만 비교하면 되는거였다
def sol(nums):
    return min(len(nums) // 2, len(set(nums)))


if __name__ == '__main__':
    nums = [3, 1, 2, 3]
    print(solution(nums))
