def test(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    alist = test(l1, l2)
    print(alist)
