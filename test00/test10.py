def romanToInt(s: str) -> int:
    start = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        # 'IV': 4,
        # 'IX': 9,
        # 'XL': 40,
        # 'XC': 90,
        # 'CD': 400,
        # 'CM': 900
    }
    tmp = 0
    num = len(s)
    for i in range(num):
        if i < num - 1 and start[s[i]] < start[s[i + 1]]:
            tmp -= start[s[i]]
        else:
            tmp += start[s[i]]
    return tmp


if __name__ == '__main__':
    s = 'MCMXCIV'
    print(romanToInt(s))
