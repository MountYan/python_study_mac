def BubbleSort(nums):
    """冒泡排序
    比较相邻的元素。如果第一个比第二个大，就交换他们两个。

    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

    针对所有的元素重复以上的步骤，除了最后一个。

    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    Arguments:
        nums {[int]} -- 排序列表
    Returns:
        [int] --  升序列表
    """
    alist = nums.copy()
    length = len(alist)
    for i in range(1, length):
        for j in range(length - i):
            if alist[j] > alist[j + 1]:
                tmp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = tmp
    return alist


if __name__ == "__main__":
    nums = [5, 4, 2, 3, 7]
    alist = BubbleSort(nums)
    print(alist)
