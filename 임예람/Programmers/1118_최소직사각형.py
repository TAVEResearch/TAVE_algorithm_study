sizes=[[60, 50], 
        [30, 70], 
        [60, 30], 
        [80, 40]] #가로세로  # 4000
# sizes=[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]  # 120

def solution(sizes):
    sizes = [sorted(i) for i in sizes] #sizes 내 리스트들을 정렬해준다.
    width = [i[0] for i in sizes] #0번째 값들을 모아준다.
    height = [i[1] for i in sizes] #1번째 값들을 모아준다.

    return max(width) * max(height) #가장 큰 값들을 곱해준다.



# def solution(sizes):
#     answer = 0

#     width = []
#     height = []

#     for size in sizes:
#         width.append(size[0]) #가로길이
#         height.append(size[1])

#     max_width = max(width)
#     max_height = max(height)

#     if max_width < width.index(max_height):
#         pass  

#     print(max_width, height)

#     return answer

solution(sizes)