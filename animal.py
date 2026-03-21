class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def perform_duty(self):
        return f"{self.name} ({self.position}) zaczyna swoją zmianę."
    
class Zookeeper(Employee):
    def __init__ (self, name):
        super().__init__(name, "Opiekun zwierząt")  

    def feed_animal(self, animal_name):
        return f"{self.name} karmi teraz zwierze o imieniu {animal_name}."


class Animal:
    """
    To jest nasza instrukcja (klasa) dla wszystkich zwierząt.
    """
    def __init__(self, name, species):
        # self to "ten konkretny zwierzak"
        self.name = name
        self.species = species

    def describe(self):
        # Ta funkcja pozwoli zwierzęciu się przedstawić
        return f"Jestem {self.name}, reprezentuję gatunek: {self.species}."

# --- SPRAWDZAMY CZY DZIAŁA ---
if __name__ == "__main__":
    testowy_zwierz = Animal("Leon", "Lew")
    print(testowy_zwierz.describe()) 

    opiekun = Zookeeper("Marek")
    print(opiekun.feed_animal("Leon"))