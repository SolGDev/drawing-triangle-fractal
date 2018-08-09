import math
import turtle

class Coordinate:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    

class Fractal:
    pen = turtle.Turtle()
    def __init__ (self, startPoint, edgeLength):
        self.edgeLength = edgeLength
        self.left, self.top, self.right = self._generateTriangle(startPoint, edgeLength)
        self.pen.speed("fastest")
        self.pen.penup()
        self.pen.setposition(startPoint.x, startPoint.y)
        self.pen.pendown()

    def _generateTriangle(self, left, length):
        top = Coordinate(left.x + length/2, left.y + math.sqrt(length**2 - (length/2)**2 ))
        right = Coordinate(left.x + length, left.y)
        return left, top, right

    def drawOuterTriangle(self):
        self.pen.left(60)
        self.pen.forward(self.edgeLength)
        self.pen.right(120)
        self.pen.forward(self.edgeLength)
        self.pen.right(120)
        self.pen.forward(self.edgeLength)
        self.pen.right(60)

    def drawInnerTriangle(self):
        newStartPoint = self._getMidPointBetween(self.left, self.top)

        self.pen.right(120)
        self.pen.penup()
        self.pen.setposition(newStartPoint.x, newStartPoint.y)
        self.pen.pendown()
        self.pen.forward(self.edgeLength / 2)
        self.pen.right(120)
        self.pen.forward(self.edgeLength / 2)
        self.pen.right(120)
        self.pen.forward(self.edgeLength / 2)
        
    def drawFractal(self, fractal, times):
        if times == 0:
            return
        
        fractal.drawInnerTriangle()
        
        newFractal = Fractal(fractal.left, (fractal.edgeLength / 2))
        self.drawFractal(newFractal, times - 1)

        newFractal = Fractal(self._getMidPointBetween(fractal.left, fractal.top), (fractal.edgeLength / 2))
        self.drawFractal(newFractal, times - 1)

        newFractal = Fractal(self._getMidPointBetween(fractal.left, fractal.right), (fractal.edgeLength / 2))
        self.drawFractal(newFractal, times - 1)

    def _getMidPointBetween(self, point1, point2):
        x = (point1.x + point2.x) / 2
        y = (point1.y + point2.y) / 2
        return Coordinate(x, y)
    
    def _getDistanceBetween(self, point1, point2):
        return math.sqrt(pow((point1.x - point2.x), 2) + pow((point1.y - point2.y), 2))


startPoint = Coordinate(-250, -200)
edgeLength = 500
times = 7

fractal = Fractal(startPoint, edgeLength)
fractal.drawOuterTriangle()
fractal.drawFractal(fractal, times)
fractal.pen.hideturtle()

turtle.done()