# quick sort (partition-exchange sort)
# O(NlogN) to O(N^2)
# O(N^2) -> e.g.) sorted list as input -> unable to divide
# quick sort is also "Unstable Sort" (p488)
import random
from typing import List

# lo (index): 0
# hi (index): len(List) - 1
def quicksort(A: List[int], lo: int, hi: int) -> None:
    def partition(lo: int, hi: int) -> int:
        pivot = A[hi]
        left = lo

        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1

        A[left], A[hi] = A[hi], A[left] # pivot -> middle point

        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot, hi)

A = [idx for idx in range(10)]
random.shuffle(A)
print(A)
quicksort(A, 0, len(A)-1)
print(A)
