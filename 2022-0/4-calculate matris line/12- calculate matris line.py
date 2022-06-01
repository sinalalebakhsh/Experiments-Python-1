import os
from re import X
os.system('cls')

class CoordinatesOfPoints:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def calculate_line_length(self):
        return ((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2) ** 0.5

    def calculate_slope_line(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)

    
    def __str__(self):
        line_length = ((self.y2 - self.y1) ** 2 + (self.x2 - self.x1) ** 2) ** 0.5
        slope_line = (self.y2 - self.y1) / (self.x2 - self.x1)
        return f'Line length= {line_length} || slope line= {slope_line}'
        
        
        

points = CoordinatesOfPoints(1,3,1,3)

print()
print(points.calculate_line_length())
print()
print(points.calculate_slope_line())
print()
print(points)
print()


class Lines:
    def __init__(self, point1, point2):
        self.point1 = {'x': point1[0], 'y':point1[1]}
        self.point2 = {'x': point2[0], 'y':point2[1]}

    def __str__(self):
        return f"line: point1=({self.point1['x']},{self.point1['y']}) point2=({self.point2['x']},{self.point2['y']}) "
        
    def length(self):
        return ((self.point2['y'] - self.point1['y'])**2 + (self.point2['x'] - self.point1['x'])**2)** 0.5

line = Lines((1, 1), (3,3))

print(line.length())
print()
