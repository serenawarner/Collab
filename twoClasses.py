class Calculator():
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def add(self):
        return self.x+self.y

def test_add():
    calc = Calculator(4, 2)
    assert calc.add() == 6