W, H, result = 8, 12, 20

from math import gcd

def solution(w, h):
    total_square = w * h
    greatest_common_divisor = gcd(w, h)
    return total_square - (w + h - greatest_common_divisor)

# 8:8 = 1:1 -> -w
# 8:16 = 1:2 ->
# 8:12 = 2:3 ->