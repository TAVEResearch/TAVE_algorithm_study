# p511
# No. 64
import heapq


def kClosest(point: list, k: int) -> list:
    heap = []
    for (x, y) in point:
        dist = x ** 2 + y + +2
        heapq.heappush(heap, (dist, x, y))
    result = []
    for _ in range(k):
        (dist, x, y) = heapq.heappop(heap)
        result.append((x, y))
    return result


print(kClosest([[1, 3], [-2, 2]], 1))
