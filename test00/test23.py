import pysnooper


@pysnooper.snoop()
def max_SubArray(nums) -> int:
    sum_ = 0
    max_ = nums[0]
    for num in nums:
        sum_ += num
        if sum_ > max_:
            max_ = sum_
        if sum_ < 0:
            sum_ = 0
    return max_


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max__ = max_SubArray(nums)
    print(max__)
