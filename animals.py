from money import Money

class Animal:
    def __init__(self, name, species, monthly_cost_val=100.0):
        self.name = name
        self.species = species
        self.monthly_cost = Money(monthly_cost_val, "PLN")
    
    def descrribe(self):
        return f"Jestem {self.name}, gatunek: {self.species}. Kosztuję {self.monthly_cost} PLN miesięcznie."
    

class Lion(Animal):
    """Dziedziczenie po Animal, dodaje ryczenie."""
    def make_sound(self):
        return f"{self.name} ryczy: Roooar!"        

class Elephant(Animal):
    """Dziedziczenie po Animal, dodaje trąbienie."""
    def make_sound(self):
        return f"{self.name} trąbi: TOOT!"
    