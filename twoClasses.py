
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius
    
    def diameter(self):
        return self.radius * 2
    
    def circumference(self):
        return 3.14 * self.radius * 2
    
    def area(self):
        return 3.14 * self.radius * self.radius
    


def test_getRadius():
    circle = Circle(4)
    assert circle.getRadius() == 4

def test_diameter():
    circle = Circle(4)
    assert circle.diameter() == 8

def test_circumference():
    circle = Circle(4)
    assert circle.circumference() == 25.12

def test_area():
    circle = Circle(4)
    assert circle.area() == 50.24