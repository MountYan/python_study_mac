# def merge(nums1, m: int, nums2, n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     tmp = [0 for i in range(m + n)]
#     i = 0
#     j = 0
#     k = 0
#     while i < m and j < n:
#         if nums1[i] <= nums2[j]:
#             tmp[k] = nums1[i]
#             i += 1
#         else:
#             tmp[k] = nums2[j]
#             j += 1
#         k += 1
#     if i == m:
#         while k < m + n:
#             tmp[k] = nums2[j]
#             k += 1
#             j += 1
#     else:
#         while k < m + n:
#             tmp[k] = nums1[i]
#             i += 1
#             k += 1
#     for i in range(0, m + n):
#         nums1[i] = tmp[i]


# def merge(nums1, m: int, nums2, n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     index = m + n - 1
#     m -= 1
#     n -= 1
#     while m >= 0 and n >= 0:
#         if nums1[m] > nums2[n]:
#             nums1[index] = nums1[m]
#             m -= 1
#         else:
#             nums1[index] = nums2[n]
#             n -= 1
#         index -= 1
#     if m < 0:
#         nums1[:n + 1] = nums2[:n + 1]
def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
