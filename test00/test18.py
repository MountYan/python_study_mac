def countAndSay(n: int) -> str:
    s = "1"
    for i in range(n - 1):
        c = s[0]
        count = 0
        s1 = ""
        for char in s:
            if char == c:
                count += 1
            else:
                s1 = s1 + str(count) + c
                c = char
                count = 1

        s = s1 + str(count) + c

    return s


if __name__ == "__main__":
    n = 5
    s = countAndSay(n)
    print(s)
