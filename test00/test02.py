import pysnooper


@pysnooper.snoop()
def sorted_squares(nums):
    a_list = list(map(lambda x: pow(x, 2), nums))
    a_list.sort()
    return a_list


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    a_list = sorted_squares(nums)
    print(a_list)
    if a_list == [0, 1, 9, 16, 100]:
        print('Good!')
