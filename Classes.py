import matplotlib.pyplot as plt

class Circle:
    def __init__(self, radius1, color1 = "blue"):

        self.radius = radius1
        self.color = color1

    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius = self.radius, fc = self.color))
        plt.axis('scaled')
        plt.show()


# Create an object RedCircle

RedCircle = Circle(10, "red")
print(RedCircle.radius)
print(RedCircle.color)

#RedCircle.drawCircle()

# Create a blue circle with 100 of radius

BlueCircle = Circle(100, "blue")
print(BlueCircle.radius)
print(BlueCircle.color)

#BlueCircle.drawCircle()


# Rectangle class for creating a rectanlge object

class Rectangle:
    def __init__(self, widht = 2, height = 3, color = 'red'):

        self.height = height
        self.width = widht
        self.color = color

    def drawRectangle(self):

        plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc = self.color))
        plt.axis('scaled')
        plt.show()

# Create a skinny rectangle

SkinnyBlueRectangle = Rectangle(2,10,'blue')
#SkinnyBlueRectangle.drawRectangle()
# Create a yello rectangle

YellowRectangle = Rectangle(20,5,'yellow')
YellowRectangle.drawRectangle()