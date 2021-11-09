"""
Least Recently Used (LRU)란 가장 오래전에 사용된 아이템을 버리는 방식

길이가 제한된 자료형이 있다면 LRU를 구현하기 쉬움

cache = collections.deque(maxlen = cacheSize)

최대 크기를 초과할 때, 가장 오래된 항목부터 제거함

주의) 입력값에 0이 포함되어 있다는 점 -> 예외처리
"""
from typing import List
from collections import deque

def solution(cache_size: int, cities: List[str]) -> int:
  elapsed: int = 0

  cache = deque(maxlen = cache_size)

  for city in cities:
    city = city.lower()

    # 캐시 히드 시 재삽입 처리
    if city in cache:
      cache.remove(city)
      cache.append(city)
      elapsed += 1
    else: # 캐시 미스 시 삽입만
      cache.append(city)
      elapsed += 5
    
  return elapsed


cache_size_list = [3, 
                   3, 
                   2, 
                   5, 
                   2, 
                   0]
cities_list = [["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"], # 50
               ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"], # 21
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"], # 60
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"], # 52
               ["Jeju", "Pangyo", "NewYork", "newyork"], # 16
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]] # 25

for cache_size, cities in zip(cache_size_list, cities_list):
  print(solution(cache_size, cities))
