import collections


def sliding(nums: list, k: int) -> list:
    if not nums:
        return nums

    r = []
    for i in range(len(nums) - k + 1):
        r.append(max(nums[i:i + k]))

    return r


def queue_sliding(nums: list, k: int) -> list:
    result = []
    # deque 선언
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue

        # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        result.append(current_max)

        # 최댓값이 윈도우에서 빠지면 초기화..
        if current_max == window.popleft():
            current_max = float('-inf')
    return result


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(queue_sliding(nums, k))
