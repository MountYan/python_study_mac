import pysnooper


@pysnooper.snoop('test01.log')
def twoSum(nums, target):
    hashmap = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]
        hashmap[num] = index
    return None


if __name__ == "__main__":
    nums = [3, 2, 3]
    target = 6
    alist = twoSum(nums, target)
    print(alist)
