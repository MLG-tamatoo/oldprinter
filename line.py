class Line():
    def __init__(self, beg, end):
        self.beg = beg
        self.end = end
        self.points = []
        changex = self.end[0]-self.beg[0]
        changey = self.end[1]-self.beg[1]
        try:
            slope = changey/changex
        except:
            slope = 0
        if changex > 0:
            for x in range(self.beg[0], self.end[0], 1):
                y = round((x-self.beg[0])*slope+self.beg[1])
                self.points.append((x, y))
                #print(y)
                #print(y)
        if changex < 0:
            for x in range(self.beg[0], self.end[0], -1):
                y = round((x-self.beg[0])*slope+self.beg[1])
                self.points.append((x, y))
                #print(y)
                #print(y)
        elif changex == 0:
            if changey > 0:
                for y in range(self.beg[1], self.end[1]):
                    self.points.append((self.beg[0], y))
            elif changey < 0:
                for y in range(self.end[1], self.beg[1]):
                    self.points.append((self.beg[0], y))
        self.points.append(end)
