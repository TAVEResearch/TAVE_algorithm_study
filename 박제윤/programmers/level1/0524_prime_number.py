# date: 2021.05.24
# author: jeiyoon
from typing import List
from itertools import combinations

# Sieve of Eratosthenes
def sieve_of_eratosthenes(c: int) -> List[int]:
    sieve = [True] * (c + 1)

    for i in range(2, int(c ** 0.5) + 1):
        if sieve[i] == True: # i is a prime number
            for j in range(i + i, c + 1, i):
                sieve[j] = False

    prime_num_list = [i for i in range(2, c + 1) if sieve[i] == True]

    return prime_num_list

def solution(nums: List[int]) -> int:
    answer = 0
    combed_tuple_sum: List[int] = [sum(p) for p in list(combinations(nums, 3))]
    max_c = max(combed_tuple_sum) # maximum size of the sieve

    prime_num_list = sieve_of_eratosthenes(max_c)

    for c in combed_tuple_sum:
        if c in prime_num_list:
            answer += 1

    return answer
