import collections


def min_window_sub_two_pointer(S: str, T: str):
    need = collections.Counter(T)
    missing = len(T)
    left = start = end = 0

    # 오른쪽 포인터 이동
    for right, char in enumerate(S, 1):
        missing -= need[char] > 0
        need[char] -= 1

        # 필요 문자가 0이면 왼쪽 포인터 이동 판단
        if missing == 0:
            while left < right and need[S[left]] < 0:
                need[S[left]] += 1
                left += 1

            if not end or right - left <= end - start:
                start, end = left, right
                need[S[left]] += 1
                missing += 1
                left += 1
    return S[start:end]


def use_Counter(s: str, t: str):
    t_count = collections.Counter(t)
    current_count = collections.Counter()

    start = float('-inf')
    end = float('inf')

    left = 0
    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        current_count[char] += 1

        # AND 연산 결과로 왼쪽 포인터 이동 판단
        while current_count & t_count == t_count:
            if right - left < end - start:
                start, end = left, right
            current_count[s[left]] -= 1
            left += 1
    return s[start:end] if end - start <= len(s) else ''


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    print(use_Counter(S, T))
