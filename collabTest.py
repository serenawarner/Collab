class Food:
    def __init__(self):
        self.cooked = False
        self.temp = "cold"

    def cook(self):
        cooked = True
        temp = "hot"
        print("Your food has been cooked.")
        return cooked

    def refridgerate(self):
        temp = "cold"
        print("Your food has been refridgerated.")
        return temp

    def warmUp(self):
        temp = "warm"
        print("Your food has been warmed up.")
        return temp



class Soup(Food):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.stirred = False
        self.salted = False
        self.slurped = False
    
    def stir(self):
        stirred = True
        print("Your",self.type,"soup is stirred.")
        return stirred

    def salt(self):
        salted = True
        print("Your", self.type,"soup has been salted.")
        return salted
    
    def slurp(self):
        slurped = True
        print("You have slurped your",self.type,"soup.")
        return slurped

def test_cook():
    food = Food()
    assert food.cook() == True

def test_refridgerate():
    food = Food()
    assert food.refridgerate() == "cold"

def test_warmUp():
    food = Food()
    assert food.warmUp() == "warm"

def test_stir():
    soup = Soup("chicken")
    assert soup.stir() == True

def test_salt():
    soup = Soup("chicken")
    assert soup.salt() == True

def test_slurp():
    soup = Soup("chicken")
    assert soup.slurp() == True

