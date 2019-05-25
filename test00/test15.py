# import pysnooper


# @pysnooper.snoop()
def searchMatrix(matrix, target):
    """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
    if len(matrix) == 0:
        return False
    row = 0  # 行
    col = len(matrix[0]) - 1  # 列
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return True
    return False


if __name__ == "__main__":
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    flag = searchMatrix(matrix, target)
    print(flag)
