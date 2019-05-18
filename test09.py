# def test(A):
#     index_dict = {}
#     for index, line in enumerate(A):
#         tmp = {}
#         index_dict[index] = tmp
#         for char in line:
#             if char in tmp:
#                 tmp[char] += 1
#             else:
#                 tmp[char] = 1
#     obj = list((set(obj) for obj in nums))
#     tmp = list(set.intersection(*obj))
#     for obj in tmp:
#         tmp = {}
#         for key, value in index_dict.items():
#             if obj == key:
#                 pass

# def test(A):
#     # 每个字符串之间字符数量的交集
#     result = []
#     # chars = [chr(97 + i) for i in range(26)]
#     obj = list((set(obj) for obj in A))
#     tmp = list(set.intersection(*obj))
#     for char in tmp:
#         count = min([word.count(char) for word in A])
#         result += [char] * count
#     return result


def test(A):
    l = []
    string = set(A[0])
    for i in string:
        l += [i] * min(list(map(lambda x: x.count(i), A)))
    return l


if __name__ == '__main__':
    nums = ["bella", "label", "roller"]
    ret = test(nums)
    print(ret)
