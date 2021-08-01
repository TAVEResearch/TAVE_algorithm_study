def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for doll in range(len(board)):
            if board[doll][i - 1] == 0:
                continue
            else:
                basket.append(board[doll][i - 1])
                board[doll][i - 1] = 0
                break
        if len(basket) >= 2:
            if basket[-2] == basket[-1]:
                answer += 2
                basket.pop()
                basket.pop()
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
