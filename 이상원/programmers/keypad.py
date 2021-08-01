def solution(numbers, hand):
    answer = ''

    def dist(cur, left, right, hand):
        # 2,5,8,0 일때
        # cur: target num
        # left: left_cur -> list
        # right: right_cur ->list
        # hand: 손

        # l_dist r_dist: 단순한 x, y 좌표에서 거리
        l_dist = abs(cur[0] - left[0]) + abs(cur[1] - left[1])
        r_dist = abs(cur[0] - right[0]) + abs(cur[1] - right[1])
        # 거리가 짧은 손이 키를 눌러야 함
        if l_dist < r_dist:
            left = cur
            ans = "L"
        elif l_dist > r_dist:
            right = cur
            ans = "R"
        # 거리가 같을 경우 어느손잡이인지에 따라 달라짐
        else:
            if hand == "right":
                right = cur
                ans = "R"
            else:
                left = cur
                ans = "L"

        return left, right, ans

    # 키패드를 가로로 두고 (0,0)이 오른손 (2,0)이 왼손으로 시작
    keypad = [
        ["*", 9, 6, 3],
        [0, 8, 5, 2],
        ["#", 7, 4, 1]
    ]
    right_cur = [0, 0]
    left_cur = [2, 0]
    # 입력받은 숫자 반복
    for i in numbers:
        # 오른손만 누르는 키패드일 경우
        if i in keypad[0]:
            cur = keypad[0][:].index(i)
            right_cur = [0, cur]
            answer += "R"
        # 왼손만 누르는 키패드일 경우
        elif i in keypad[2]:
            cur = keypad[2][:].index(i)
            left_cur = [2, cur]
            answer += "L"
        # 2 5 8 0일 경우 거리 비교로 해결
        else:
            cur = keypad[1][:].index(i)
            left_cur, right_cur, ans = dist([1, cur], left_cur, right_cur, hand)
            answer += ans

    return answer


# 성공

if __name__ == '__main__':
    num = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    print(solution(num, hand))
    print('LRLLLRLLRRL')
