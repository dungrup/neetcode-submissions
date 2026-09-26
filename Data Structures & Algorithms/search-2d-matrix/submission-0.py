class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            row_idx = (top + bottom) // 2
            if target > matrix[row_idx][-1]:
                top = row_idx + 1
            elif target < matrix[row_idx][0]:
                bottom = row_idx - 1
            else:
                break

        if not (top <= bottom):
            return False

        row_idx = (top + bottom) // 2
        l, r = 0, COLUMNS - 1
        while l <= r:
            mid = (l + r) // 2
            val2 = matrix[row_idx][mid]
            if val2 < target:
                l = mid + 1
            elif val2 > target:
                r = mid - 1
            else:
                return True

        return False
