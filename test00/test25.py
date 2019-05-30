def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    # return bin(int(a, 2) + int(b, 2))[2:]
    res = ""
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0 or carry:
        tmp1 = int(a[i]) if i >= 0 else 0
        tmp2 = int(b[j]) if j >= 0 else 0
        carry, t = divmod(tmp1 + tmp2 + carry, 2)
        res = str(t) + res
        i -= 1
        j -= 1
    return res


if __name__ == "__main__":
    a = "11"
    b = "1"
    print(addBinary(a, b))
