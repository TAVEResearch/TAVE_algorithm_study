import heapq


def queue_recon(people: list) -> list:
    # 그리디 문제의 대부분은 우선순위 큐를 이용한다
    heap = []
    # 키 역순, 인덱스 삽입
    for person in people:
        print(-person[0])
        heapq.heappush(heap, (-person[0], person[1]))
    print(heap)
    result = []
    # 키 역순, 인덱스 추출
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    return result


if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(queue_recon(people))
