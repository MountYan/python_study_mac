# def diStringMatch(S: str):
#     left = 0
#     right = len(S)
#     A = []
#     for x in S:
#         if x == "I":
#             A.append(left)
#             left += 1
#         else:
#             A.append(right)
#             right -= 1
#     A.append(right)
#     return A


# if __name__ == '__main__':
#     S = "IDID"
#     alist = diStringMatch(S)
#     print(alist)
def test(s):
    length = len(s) + 1
    A = list(range(length))
    alist = []
    for index, x in enumerate(s):
        if x == "I":
            tmp = A[0]
            alist.append(tmp)
            A.remove(tmp)
        else:
            tmp = A.pop()
            alist.append(tmp)
    alist.extend(A)
    return alist


if __name__ == '__main__':
    s = "IDID"
    alist = test(s)
    print(alist)
