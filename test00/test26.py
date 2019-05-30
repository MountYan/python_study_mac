class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        while start <= end:
            mid = (start + end) // 2
            if mid**2 <= x and (mid + 1)**2 > x:
                return mid
            elif mid**2 > x:
                mid -= 1
            else:
                mid += 1
        return mid


if __name__ == '__main__':
    x = 4
    r = Solution().mySqrt(x)
    print(r)
