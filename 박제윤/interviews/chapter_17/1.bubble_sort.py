# Bubble sort
# O(N^2)
import random
from typing import List

def bubblesort(A:List[int]) -> List[int]:
    for i in range(1, len(A)):
        for j in range(0, len(A)-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A

A = [idx for idx in range(10)]
random.shuffle(A)
print(A)
print(bubblesort(A))
