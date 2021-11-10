# n (10진법)	n (3진법)	앞뒤 반전(3진법)	10진법으로 표현
# 45	        1200	    0021	            7
n=45 #7

def solution(n):
    answer = 0

    nums = ""
    while(True):
        if n < 3:
            nums += str(n)
            break
        elif (n / 3) != 0: #안 나눠지면
            nums += str(n % 3)
            n = n // 3
        else: #나눠지면
            nums += str(0)
            n = n // 3

    return int(nums, 3) #3진법을 10진법으로 바꿔준다.

print(solution(n))