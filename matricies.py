class Matrix:
    def __init__(self, rows, columns):
        self.matrix = []
        for y in range(0, rows):
            row = []
            for x in range(0, columns):
                row.append(0)
            self.matrix.append(row)
        self.rows = []
        self.columns = []
        for row in self.matrix:
            self.rows.append(row)
        for i in range(0, columns):
            column = []
            for row in self.rows:
                column.append(row[i])
            self.columns.append(column)

    def Refresh(self, newrows, lencols):
        self.rows = newrows
        self.matrix = newrows
        self.columns = []
        for i in range(0, lencols):
            column = []
            for row in self.rows:
                column.append(row[i])
            self.columns.append(column)
        return self

def Multiply(A, B):
    C = Matrix(len(A.rows), len(B.columns))
    for r in range(0, len(A.rows)):
        row = A.rows[r]
        for c in range(0, len(B.columns)):
            column = B.columns[c]
            sum = 0
            for j in range(0, len(row)):
                sum += round(row[j] * column[j])
            C.rows[r][c] = sum
    C.Refresh(C.rows, len(C.columns))
    return C


def OneVarDiv(A, div):
    for r in range(0, len(A.rows)):
        row = A.rows[r]
        for c in range(0, len(row)):
          if div != 0:
            A.rows[r][c] = round(A.rows[r][c] / div)
          else:
            A.rows[r][c] = round(A.rows[r][c] / 1)
    A.Refresh(A.rows, len(A.columns))
    return A


def ThreeDPointsToMatrices(points):
    matricies = []
    for point in points:
        xyz = [[point.x], [point.y], [point.z], [1]]
        pntmatrix = Matrix(4, 1)
        pntmatrix.Refresh(xyz, 1)
        matricies.append(pntmatrix)
    return matricies

def Turn3dMatriciesTo2DPoints(THdmatricies, Zdisplay, Zeye, H):
    TWdmatricies = []
    for matrix in THdmatricies:
        Zobject = matrix.rows[2][0]
        if(Zobject == 0):
          r = 1
        else:
          r = 1 / Zobject
        Inverse = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, -r, 1]]
        matrixA = Matrix(4, 4)
        matrixA.Refresh(Inverse, len(Inverse[0]))
        TWdmatrix = OneVarDiv(Multiply(matrixA, matrix), 1 - r*Zdisplay)
        TWdmatricies.append(TWdmatrix)
    TWdpoints = []
    for matrix in TWdmatricies:
        point = (round(matrix.rows[0][0]), round(matrix.rows[1][0]))
        TWdpoints.append(point)
    return TWdpoints