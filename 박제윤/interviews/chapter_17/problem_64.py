# page: p511
# sol) Euclidean Distance
import heapq
from typing import List

def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
  heap = []
  for (x, y) in points:
    dist = x**2 + y**2
    heapq.heappush(heap, (dist, x, y))

  result = []

  for _ in range(K):
    (dist, x, y) = heapq.heappop(heap)
    result.append((x,y))

  return result

# output = [[-2, 2]]
points = [[1, 3], [-2, 2]]
K = 1

# output = [[3, 3], [-2, 4]]
# points = [[3, 3], [5, -1], [-2, 4]]
# K = 2
print(kClosest(points, K))

