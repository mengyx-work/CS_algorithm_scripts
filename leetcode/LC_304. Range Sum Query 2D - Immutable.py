class NumMatrix(object):

    def __init__(self, matrix):
        rowN = len(matrix)
        colN = len(matrix[0]) if rowN > 0 else 0
        self.sumMatrix = []
        arr, curSum = [], 0
        for i in range(colN):
            curSum += matrix[0][i]
            arr.append(curSum)
        self.sumMatrix.append(arr)

        for i in range(1, rowN):
            arr, curSum = [], 0
            for j in range(colN):
                curSum += matrix[i][j]
                arr.append(curSum + self.sumMatrix[i-1][j])
            self.sumMatrix.append(arr)

    def sumRegion(self, row1, col1, row2, col2):
        D = self.sumMatrix[row2][col2]
        A = None
        if row1 == 0:
            A, B = 0, 0
        else:
            B = self.sumMatrix[row1-1][col2]

        if col1 == 0:
            A, C = 0, 0
        else:
            C = self.sumMatrix[row2][col1-1]

        if A is None:
            A = self.sumMatrix[row1-1][col1-1]
        # print(self.sumMatrix)
        return D - B - C + A

# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
matrix = [[]]
obj = NumMatrix(matrix)
# assert obj.sumRegion(2, 1, 4, 3) == 8
# assert obj.sumRegion(1, 1, 2, 2) == 11
# assert obj.sumRegion(1, 2, 2, 4) == 12