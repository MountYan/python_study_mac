# def test(strs):
#     str_dict = {}
#     for line in strs:
#         tmp = 0
#         if tmp < len(line):
#             tmp = len(line)
#             str_dict[tmp] = line
#     min_index = sorted(str_dict.keys()).pop(0)
#     min_str = str_dict[min_index]
#     return min_str


def test(strs):
    '''
    Python 特性，取每一个单词的同一位置的字母，看是否相同。
    '''
    res = ""
    for tmp in zip(*strs):
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    return res


def test2(s):
    '''
    取一个单词 s，和后面单词比较，看 s 与每个单词相同的最长前缀是多少！遍历所有单词
    '''
    if not s:
        return ""
    res = s[0]
    i = 1
    while i < len(s):
        while s[i].find(res) != 0:
            # 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
            res = res[0:len(res) - 1]
        i += 1
    return res


def test3(s):
    '''
    按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同。
    '''
    if not s:
        return ""
    # s.sort()
    n = len(s)
    a = s[0]
    b = s[n - 1]
    res = ""
    for i in range(len(a)):
        if i < len(b) and a[i] == b[i]:
            res += a[i]
        else:
            break
    return res


if __name__ == '__main__':
    strs = ["flower", "fow", "flight"]
    ret = test(strs)
    print(ret)
