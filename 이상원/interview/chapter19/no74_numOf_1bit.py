def NOF1Bit(unInt):
    return bin(unInt).count('1')


if __name__ == '__main__':
    input_data = 00000000000000000000000000001011
    print(NOF1Bit(input_data))
