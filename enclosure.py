class Enclosure:
    """Wybieg dla zwierząt"""
    
    def __init__(self, name):
        self.name = name 
        self.animals = []

    def add_animal(self,animal):
        self.animals.append(animal)
        print (f"Dodano {animal.name} ({animal.species}) do wybiegu: {self.name}")

    def __len__(self):
        return len(self.animals)
    
    def __iter__(self):
        return iter(self.animals)
    
    def total_maintenance_cost(self):
        if not self.animals:
            return None
        
        total = self.animals[0].monthly_cost
        for animal in self.animals[1:]:
            total += animal.monthly_cost
            return total
