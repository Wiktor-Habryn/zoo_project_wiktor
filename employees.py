from money import Money

class Employee:

    def __init__(self, name, position, salary_val = 3000.0):
        self.name = name
        self.position = position
        self.salary = Money(salary_val, "PLN")

    def perform_duty(self):
        return f"{self.name} ({self.position}) rozpoczyna swoją zmianę."
    
    def __str__(self):
        return f"Pracownik: {self.name}, stanowisko: {self.position}, pensja: {self.salary}"
    
class Zookeeper(Employee):
    
    """Opiek zwierząt, dzieciczy po employee"""
    
    def __init__(self, name, salary_val=3500.0):
        super().__init__(name, "Opiekun zwierząt", salary_val)

    def feed_animal(self, animal_name):
        return f"{self.name} karmi teraz zwierzę: {animal_name}."
    
class Vet(Employee):

    """Weterynarz, dzieciczy po employee"""
    
    def __init__(self, name, salary_val=5200.0):
        super().__init__(name, "Weterynarz", salary_val)

    def heal_animal(self, animal_name):
        return f"{self.name} leczy teraz zwierze: {animal_name}."