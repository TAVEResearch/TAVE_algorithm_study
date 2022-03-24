from collections import deque


def case(step):
    start = []
    result = True
    for line in range(5):
        for idx in range(5):
            if step[line][idx] == 'P':
                start.append([line, idx])
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited = [[False]*5 for _ in range(5)]
        cnt = 0

        while queue:
            x, y = queue.popleft()
            visited[x][y] = True

            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                # 미로 찾기 공간을 벗어날 경우 무시
                if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                    continue
                if visited[nx][ny]:
                    continue
                # # 벽인 겨우 무시
                if step[nx][ny] == 'X':
                    continue
                if step[nx][ny] == 'P':
                    return False
                queue.append((nx, ny))
            cnt += 1
            if cnt == 2:
                return True
        return True
    for x, y in start:
        if not bfs(x, y):
            result = False
            break
    return result


def solution(place):
    answer = []
    for item in place:
        if case(item):
            answer.append(1)
        else:
            answer.append(0)
    return answer


if __name__ == '__main__':
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                             "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))
