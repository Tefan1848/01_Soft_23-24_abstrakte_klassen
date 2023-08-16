from abc import ABC, abstractmethod

class AbstrakteKlasse(ABC):
    def __init__(self, attribut):
        self.attribut = attribut

    def normale_methode(self):
        print("Normale Methode aufrufen")

@abstractmethod
def abstrakte_methode(self):
    pass

class AbgeleiteteKlasse(AbstrakteKlasse):
    def abstrakte_methode(self):
        print("Implemtierung der vormals abstrakten Methode")

    def normale_methode(self):
        print("Test")

testobjekt = AbgeleiteteKlasse("test")