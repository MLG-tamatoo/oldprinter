import math
import line
import matricies

class Node:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    
class Cube:
  def __init__(self, cubeorigin, base, height, thickness):
    self.cubeorigin = cubeorigin
    self.base = base
    self.height = height
    self.lines = []
    self.TWdpoints = []
    self.backofcube = []
    self.frontofcube = [
        Node(cubeorigin[0], cubeorigin[1], cubeorigin[2]), Node(cubeorigin[0], cubeorigin[1] + height, cubeorigin[2]), Node(cubeorigin[0] + base, cubeorigin[1] + height, cubeorigin[2]),
        Node(cubeorigin[0] + base, cubeorigin[1], cubeorigin[2])]
    print("created front of cube")
    for point in self.frontofcube:
        self.backofcube.append(Node(point.x, point.y, point.z+thickness))
    print("created back of cube")
    self.points = []
    for point in self.frontofcube:
        self.points.append(point)
    for point in self.backofcube:
        self.points.append(point)
    print("created all main points of cube")
      
  def FindCenter(self):
    num_points = len(self.points)
    meanX = sum([point.x for point in self.points]) / num_points
    meanY = sum([point.y for point in self.points]) / num_points
    meanZ = sum([point.y for point in self.points]) / num_points
    return (meanX, meanY, meanZ)
    
  #https://www.petercollingridge.co.uk/tutorials/3d/pygame/rotation/
  def rotateZ(self, center, radians): 
    cx = center[0]
    cy = center[1]
    cz = center[2]
    for point in self.points:
        x      = point.x - cx
        y      = point.y - cy
        d      = math.hypot(y, x)
        theta  = math.atan2(y, x) + radians
        point.x = cx + d * math.cos(theta)
        point.y = cy + d * math.sin(theta)

  def rotateX(self, center, radians):
    cx = center[0]
    cy = center[1]
    cz = center[2]
    for point in self.points:
        y      = point.y - cy
        z      = point.z - cz
        d      = math.hypot(y, z)
        theta  = math.atan2(y, z) + radians
        point.z = cz + d * math.cos(theta)
        point.y = cy + d * math.sin(theta)
      
  def rotateY(self, center, radians):
    cx = center[0]
    cy = center[1]
    cz = center[2]
    for point in self.points:
        x      = point.x - cx
        z      = point.z - cz
        d      = math.hypot(x, z)
        theta  = math.atan2(x, z) + radians
        point.z = cz + d * math.cos(theta)
        point.x = cx + d * math.sin(theta)
      
  def AddCubeValues(self, frame, points):
    for point in points:
      try:
        frame[point[1]][point[0]] = "&"
      except:
        break
  def RemoveCubeValues(self, frame, points):
    for point in points:
      try:
        frame[point[1]][point[0]] = " "
      except:
        break
        
  def Get2DCords(self, Zdisplay, Zeye, H):
    THdmatricies = matricies.ThreeDPointsToMatrices(self.points)
    TWdpoints = matricies.Turn3dMatriciesTo2DPoints(THdmatricies, Zdisplay, Zeye, H)
    print('calculated 2d cords')
    return TWdpoints
    
  def CreateLines(self):
    self.lines = []
    #front and back
    for i in range(0, 3):  
      newline = line.Line(self.TWdpoints[i], self.TWdpoints[i+1])
      self.lines.append(newline)
      
    newline = line.Line(self.TWdpoints[0], self.TWdpoints[3])
    self.lines.append(newline)
    
    for i in range(4, 7):  
      newline = line.Line(self.TWdpoints[i], self.TWdpoints[i+1])
      self.lines.append(newline)
    newline = line.Line(self.TWdpoints[4], self.TWdpoints[7])
    self.lines.append(newline)

    newline = line.Line(self.TWdpoints[0], self.TWdpoints[4])
    self.lines.append(newline)
    newline = line.Line(self.TWdpoints[1], self.TWdpoints[5])
    self.lines.append(newline)
    newline = line.Line(self.TWdpoints[2], self.TWdpoints[6])
    self.lines.append(newline)
    newline = line.Line(self.TWdpoints[3], self.TWdpoints[7])
    self.lines.append(newline)
      

