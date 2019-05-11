# import pysnooper
import random
import string
from wrap_time import time_this_function


# @pysnooper.snoop()
def common_element_count(nums_list: list):
    print(nums_list)
    if all(nums_list):
        nums = list(map(lambda x: set(x), nums_list))
        set_element = set.intersection(*nums)
        return len(set_element), set_element
    else:
        return 0


def gerate_nums_list():
    elements = string.digits + string.ascii_lowercase + string.ascii_uppercase
    print(elements)
    nums_list = []
    for _ in range(4):
        nums = random.choices(elements, k=4)
        nums_list.append(nums)
    return nums_list


@time_this_function
def main():
    nums_list = gerate_nums_list()
    count, set_element = common_element_count(nums_list=nums_list)
    number = 1
    while 1:
        if count >= 1:
            break
        else:
            nums_list = gerate_nums_list()
            count, set_element = common_element_count(nums_list=nums_list)
            number += 1

    return number, count, set_element


if __name__ == '__main__':
    # 4个列表，4个元素，随机生成
    number, count, set_element = main()
    print(f'循环次数为{number}，共同元素数量为{count}，共同元素为{set_element}')
