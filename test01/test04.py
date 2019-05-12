def reverse(x: int) -> int:
    str_x = str(x)
    flag = False
    if str_x.startswith('-'):
        flag = True
        str_x = str_x.replace('-', '')
    tmp = ''.join(list(reversed(str_x)))
    if flag:
        tmp = '-' + tmp
    tmp = int(tmp)
    if tmp < -2**31 or tmp + 1 > 2**31:
        return 0
    return tmp


if __name__ == "__main__":
    x = 1534236469
    tmp = reverse(x)
    print(tmp)
