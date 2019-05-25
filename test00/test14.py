# def removeElement(nums, val) -> int:
#     i = 0
#     while i < len(nums):
#         if nums[i] == val:
#             nums.pop(i)
#             i -= 1
#         else:
#             i += 1
#     return len(nums)


# def removeElement(nums, val) -> int:
#     i = 0
#     for j in range(len(nums)):
#         if nums[j] != val:
#             nums[i] = nums[j]
#             i += 1
#     return i
def removeElement(nums, val) -> int:
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return i


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    ret = removeElement(nums, val)
    print(ret)
