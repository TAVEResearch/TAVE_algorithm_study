# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    keypad = [
        ['*', 0, '#'],
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3]
    ]
    left = [0, 0]
    right = [0, 2]
    # 숫자 3으로 나워서 나머지가 1이냐 0이냐로 오른손 왼손 분류
    left_hand = list(zip(*keypad))[0]
    right_hand = list(zip(*keypad))[2]
    mid = list(zip(*keypad))[1]

    for i in numbers:
        print(f'i: {i}------------')
        if i % 3 == 1:
            # left
            left[0] = left_hand.index(i)
            left[1] = 0
            print(f'left:{left} right:{right}')
            answer += "L"
        elif i % 3 == 0:
            # right
            right[0] = right_hand.index(i)
            right[1] = 2
            print(f'left:{left} right:{right}')
            answer += "R"
        else:
            # 2 5 8 0
            # TODO: 가로 세로 1칸씩인거 생각하기, 가까운 손가락 찾기
            cur = mid.index(i)
            if abs(left[0] - cur) <= 1 and abs(left[1] - 1) <= 1 and (
                    left[0] - cur) * (left[1] - 1) == 0:
                left[0] = cur
                left[1] = 1
                answer += "L"
                print(f'left:{left} right:{right}')
            elif abs(right[0] - cur) <= 1 and abs(right[1] - 1) <= 1 and (
                    right[0] - cur) * (right[1] - 1) == 0:
                right[0] = cur
                right[1] = 1
                answer += "R"
                print(f'left:{left} right:{right}')

    return answer


def solution_l(numbers, hand):
    answer = ''

    def compare(a: list, b: list):
        if abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1 and (a[0] - b[0]) * \
                (a[1] - b[1]) == 0:
            return True
        else:
            return pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2)

    keypad = [
        ["*", 9, 6, 3],
        [0, 8, 5, 2],
        ["#", 7, 4, 1]
    ]
    left_start = [2, 0]
    right_start = [0, 0]

    for i in numbers:
        if i in keypad[0]:
            cur = keypad[0][:].index(i)
            cur_li = [0, cur]
            right_start = cur_li
            answer += "R"
        elif i in keypad[2]:
            cur = keypad[2][:].index(i)
            cur_li = [2, cur]
            left_start = cur_li
            answer += "L"
        else:
            cur = keypad[1][:].index(i)
            cur_li = [1, cur]
            if compare(cur_li, left_start) == True and compare(cur_li,
                                                               right_start) == True:
                if hand == "right":
                    right_start = cur_li
                    answer += "R"
                else:
                    left_start = cur_li
                    answer += "L"
            elif compare(cur_li, left_start) == True:
                left_start = cur_li
                answer += "L"
            elif compare(cur_li, right_start) == True:
                right_start = cur_li
                answer += "R"
            else:
                if compare(cur_li, left_start) < compare(cur_li, right_start):
                    left_start = cur_li
                    answer += "L"
                elif compare(cur_li, left_start) > compare(cur_li, right_start):
                    right_start = cur_li
                    answer += "R"
                else:
                    if hand == "right":
                        right_start = cur_li
                        answer += "R"
                    else:
                        left_start = cur_li
                        answer += "L"
    return answer


if __name__ == '__main__':
    num = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution_l(num, hand))
    print('LRLLLRLLRRL')
