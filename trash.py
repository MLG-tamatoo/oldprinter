"""def UpdateLines(self):
    self.lines = []
    #front
    for i in range(0, len(self.frontofcubeTWd)-1):
      newline = line.Line(self.frontofcubeTWd[i], self.frontofcubeTWd[i+1])
      self.lines.append(newline)
    self.lines.append(line.Line(self.frontofcubeTWd[0], self.frontofcubeTWd[len(self.frontofcubeTWd)-1]))
    #back
    for i in range(0, len(self.backofcubeTWd)-1):
      newline = line.Line(self.backofcubeTWd[i], self.backofcubeTWd[i+1])
      self.lines.append(newline)
    self.lines.append(line.Line(self.backofcubeTWd[0], self.backofcubeTWd[len(self.backofcubeTWd)-1]))
    #connecting
    for i in range(0, len(self.frontofcubeTWd)):
      newline = line.Line(self.frontofcubeTWd[i], self.backofcubeTWd[i])
      self.lines.append(newline)"""

"""def RotateTHdMatrix(matrix, phi, theta, yaw):
  Rx = [[1, 0, 0, 0], [0, math.cos(phi), -1*math.sin(phi), 0], [0, math.sin(phi), math.cos(phi), 0], [0, 0, 0, 1]]
  Ry = [[math.cos(theta), 0, math.sin(theta), 0], [0, 1, 0, 0], [-1*math.sin(theta), 0, math.cos(theta), 0], [0, 0, 0, 1]]
  Rz = [[math.cos(yaw), -1*math.sin(yaw), 0, 0], [math.sin(yaw), math.cos(yaw), 0, 0], [0, 0, 1, 0], [0,0,0,1]]

  xrmatrix = Matrix(4, 4).Refresh(Rx, 4)
  yrmatrix = Matrix(4, 4).Refresh(Ry, 4)
  zrmatrix = Matrix(4, 4).Refresh(Rz, 4)
  newmatrix = Multiply(xrmatrix, matrix)
  newmatrix = Multiply(zrmatrix, Multiply(yrmatrix, Multiply(xrmatrix, matrix)))
  return newmatrix"""

"""def RotateTHdMatricies(matricies, phi, theta, yaw):
  newmatricies = []
  for matrix in matricies:
    rotatedmatrix = RotateTHdMatrix(matrix, phi, theta, yaw)
    newmatricies.append(rotatedmatrix)
  return newmatricies"""


"""

cube = Cube((0,0,0.1), 10, 10, 10)
print(f"front of cube 3-d {cube.frontofcube}")
print(f"back of cube 3-d {cube.backofcube}")

frontmatricies = ThreeDPointsToMatrices(cube.frontofcube)
backmatricies = ThreeDPointsToMatrices(cube.backofcube)


phi = 0
theta = 0
yaw = 0
cube.frontofcubeTWd = Turn3dMatriciesTo2D(frontmatricies, Zdisplay, Zeye, H)
cube.backofcubeTWd = Turn3dMatriciesTo2D(backmatricies, Zdisplay, Zeye, H)
print(f"front of cube 2-d {cube.frontofcubeTWd}")
print(f"back of cube 2-d {cube.backofcubeTWd}")"""
