class Box:
  def __init__(self, base, height, xoffset, yoffset):
    self.points = []
    self.base = base
    self.height = height
    self.xvelocity = 0
    self.yvelocity = 0
    for x in range(0, base):
      for y in range(0, height):
        self.points.append((x+xoffset, y+yoffset))

  def AddBoxValues(self, frame):
    for point in self.points:
      try:
        frame[point[1]][point[0]] = "*"
      except:
        break
  def RemoveBoxValues(self, frame):
    for point in self.points:
      try:
        frame[point[1]][point[0]] = " "
      except:
        break
