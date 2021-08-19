def H_distance(x: int, y: int) -> int:
    return bin(x ^ y).count('1')


print(H_distance(1, 4))
