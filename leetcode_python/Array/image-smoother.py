# Time:  O(m * n)
# Space: O(1)

# Given a 2D integer matrix M representing the gray scale of an image,
# you need to design a smoother to make the gray scale of each cell becomes
# the average gray scale (rounding down) of all the 8 surrounding cells and itself.
# If a cell has less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# Note:
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].



# V1  : dev 



# V2 

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                current = 0
                count = 0
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        row = i + a
                        col = j + b
                        if 0 <= row < m and 0 <= col < n:
                            current += M[row][col]
                            count += 1
                result[i][j] = math.floor(current / count)
        return result


# V2 
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def getGray(M, i, j):
            total, count = 0, 0.0
            for r in range(-1, 2):
                for c in range(-1, 2):
                    ii, jj = i + r, j + c
                    if 0 <= ii < len(M) and 0 <= jj < len(M[0]):
                        total += M[ii][jj]
                        count += 1.0
            return int(total / count)

        result = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                result[i][j] = getGray(M, i, j);
        return result




