
def PrintFrame(frame):
    pic = []
    for line in frame:
        pic.append("".join(line))
        #print("".join(line))
    print("\n".join(pic))

def CreateFrame(base, height):
  lines = []
  for y in range(0, height+1):
    line = []
    for x in range(0, base):
      line.append(" ")
    lines.append(line)
  return lines

def Straight(frame, draw_lines):
  for line in draw_lines:
    for point in line:
      try:
        frame[point[1]][point[0]] = "|"
      except:
        break

def UnderScore(base, height, draw_lines, frame):
  for x in range (0, base):
    for y in range(0, height+1):
      for draw_line in draw_lines:
        for point in draw_line:
          if x != point[0]:
            if y != point[1]:
              frame[y][x] = (" ")

def CreateEdge(base, height):
  #setup box values
  draw_lines = []
  top_line = []
  for i in range(0, base):
    top_line.append((i, 0))

  bottom_line = []
  for i in range(0, base):
    bottom_line.append((i, height))

  left_line = []
  for i in range(0, height):
    left_line.append((0, i))

  right_line = []
  for i in range(0, height):
    right_line.append((base-1, i))

  draw_lines = [left_line, right_line, top_line, bottom_line]
  return draw_lines
