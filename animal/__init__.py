class mammal:
    paw: int
    hair: bool
    lactate: bool
    color: str
    speak: str
    genere: str

    def __init__(self,color, genere):
        self.paw = 4
        self.hair = True
        self.lactate = True
        self.color = color
        self.genere = genere 
    def info(self):
        print(self.genere + "\t" + self.speak + "\t" + str(self.paw)+ "\t" + str(self.hair) + "\t" + str(self.lactate) + "\t" + self.color)

class oviparous:
    paw: int
    feather: bool
    color: str
    speak: str
    genere: str

    def __init__(self,color, genere):
        self.paw = 2
        self.feather = True
        self.color = color
        self.genere = genere 
    def info(self):
        print(self.genere + "\t" + self.speak + "\t" + str(self.paw)+ "\t" + str(self.feather) + "\t" + "\t" + self.color)        
class feline(mammal):
    speak: str
    def __init__(self,color):
        super().__init__(color, "feline")
        self.speak = "Miau!"

class canine(mammal):
    speak: str
    def __init__(self,color):
        super().__init__(color, "canine")
        self.speak = "Waou!"

class bird(oviparous):
    speak: str
    def __init__(self,color):
        super().__init__(color, "bird")
        self.speak = "Pio!"
