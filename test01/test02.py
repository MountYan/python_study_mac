def climbStairs(n: int):
    '''
    dp[i] = dp[i-1] + dp[i-2]
    '''
    a, b = 1, 2
    if n == 1:
        return 1
    if n == 2:
        return 2
    for i in range(2, n):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    n = 35
    print(climbStairs(n))
