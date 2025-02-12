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
