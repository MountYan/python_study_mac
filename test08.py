def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    tmp = 0
    while x > tmp:
        tmp = tmp * 10 + x % 10
        x //= 10
    return x == tmp or x == tmp // 10


if __name__ == '__main__':
    x = 121
    flag = isPalindrome(x)
    print(flag)
