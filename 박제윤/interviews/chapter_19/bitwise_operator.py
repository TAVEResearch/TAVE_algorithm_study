# page: p542

# ^: XOR
print(True ^ True)

# ~
# two's complement
# e.g.) -12 = Not 12 + 1
# So, "~": Not x = -x - 1 
print(~ True)

# 1) ~0b1100 -> 0b0011 -> 0b0010
# 2) -ob1100 -> bin(0b1100 ^ 0b1111) : using MASK
print(bin(0b0101 ^ ~0b1100))

print(bin(87))
print(int('1010111', 2))

a = bin(87)
print(type(a))

b = 0b1010111
print(type(b))

c = 0x57 # hex(87)
print(c)

print(id(87))
print(id(b))
print(id(c))
