def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            nums[i + 1] = nums[j]
            i += 1
    return i + 1 if nums else 0


if __name__ == '__main__':
    nums = [1, 1, 2]
    i = removeDuplicates(nums)
    print(i)
