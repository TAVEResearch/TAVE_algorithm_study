# p.83
import collections


def dynamic(nums: list):
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)

        if counts[num] > len(nums) // 2:
            return num


def solution(nums: list):
    if not nums:
        return None
    if len(nums):
        return nums[0]

    half = len(nums) // 2
    a = solution(nums[:half])
    b = solution(nums[half:])

    return [b, a][nums.count(a) > half]


if __name__ == '__main__':
    in_ = [2, 2, 1, 1, 1, 2, 2]
    print(solution(in_))
