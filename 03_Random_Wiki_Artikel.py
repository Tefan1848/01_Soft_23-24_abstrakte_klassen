from abc import ABC, abstractmethod

class Sportler(ABC):
    @abstractmethod

    def erfolge(self):
        pass

    def sportart(self):
        pass

class Luke_Jarrod_McKenzie(Sportler):

    def __init__(self, name):
        self.name = name

    def erfolge(self):
        return "3. Rang ITU-Weltmeisterschaft Triathlon Junioren \n9 × Ironman-Sieger \nZweiter Ironman Hawaii "

    def sportart(self):
        return "Fahrradfahrer"

sportler = Luke_Jarrod_McKenzie("Luke Jarrod McKenzie")
print(sportler.erfolge())
print(sportler.sportart())
