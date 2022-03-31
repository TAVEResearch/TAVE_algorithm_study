numbers = [5,8,4,0,6,7,9]

def solution(numbers):
    answer = 45
    numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers.sort() #[0, 4, 5, 6, 7, 8, 9]
    result = 0

    # print(numbers)

    for give_num in numbers:
        for check_num in numberList:
            #주어진 값을 정렬했기 때문에 numberList의 값보다 크거나 같다면
            #무조건 더해야할 값이니까 이 이상 체크하지 않고 넘어감.
            if give_num == check_num:
                answer -= give_num
            else:
                pass
    return answer

print(solution(numbers))
# solution(numbers)

#다른 사람 풀이
def solution(numbers):
    return 45 - sum(numbers)