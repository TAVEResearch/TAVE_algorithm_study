import random
from typing import List

def quicksort(A: List[int], lo: int, hi: int) -> List[int]:
    def partition(lo: int, hi: int) -> int:
        pivot = A[hi]
        left = lo

        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1

        A[left], A[hi] = A[hi], A[left]

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
