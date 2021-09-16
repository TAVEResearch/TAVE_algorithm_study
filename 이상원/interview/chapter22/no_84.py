# p.616

def diffWayToCompute(input: str) -> list:
    def compute(left, right, op):
        result = []
        for l in left:
            for r in right:
                result.append(eval(str(l) + op + str(r)))
        return result

    if input.isdigit():
        return [int(input)]

    results = []
    for idx, value, in enumerate(input):
        if value in "-+*":
            left = diffWayToCompute(input[:idx])
            right = diffWayToCompute(input[idx + 1:])

            results.extend(compute(left, right, value))
    return results


if __name__ == '__main__':
    _in = '2-1-1'
    print(diffWayToCompute(_in))
