# def plusOne(digits):
#     if not digits:
#         return [1]
#     else:
#         if digits[-1] == 9:
#             tmp = int(''.join(list(map(str, digits)))) + 1
#             return list(map(int, list(str(tmp))))
#         else:
#             digits.append(digits.pop() + 1)
#             return digits


def plusOne(digits):
    if not digits:
        return [1]
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + [0] * len(digits)


if __name__ == '__main__':
    digits = [8, 9]
    print(plusOne(digits))
