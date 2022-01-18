arr = [1,1,3,3,0,1,1]	
answer = [1,3,0,1]
def solution(arr):
    answer = []
    for idx, num in enumerate(arr):
        if idx != (len(arr)-1):
            if num != arr[idx+1]:
                answer.append(num)
        else:
            if num == arr[idx-1]:
                answer.append(num)
    return answer
print(solution(arr))