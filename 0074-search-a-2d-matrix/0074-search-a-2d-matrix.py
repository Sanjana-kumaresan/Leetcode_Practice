class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        row = len(matrix)       
        col = len(matrix[0]) 
        beg = 0
        end = row*col
        while beg < end:
            mid = beg + (end - beg) // 2
            idx = matrix[mid / col][mid % col];
            if idx == target:
                return True
            if idx < target:
                beg = mid + 1
            else:
                end = mid
        return False 