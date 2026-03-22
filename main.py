#1. Import z modułów
from animals import Lion, Elephant
from employees import Zookeeper, Vet
from enclosure import Enclosure
from money import Money

def main():
    print("Witaj w systemie zarządzania zoo.\n")

#2. Wybieg

    wybieg_afryka = Enclosure("Sawanna")

#3. Zwierzęta

    simba = Lion("Simba", "Lew", monthly_cost_val=600.0)
    nala = Lion("Nala", "Lew", monthly_cos_val=550.0)
    dumbo = Elephant("Dumbo", "Słoń", monthly_cost_val=1200.0)

#4. Zwierzęta do wybiegu

    wybieg_afryka.add_animal(simba)
    wybieg_afryka.add_animal(nala)
    wybieg_afryka.add_animal(dumbo)

#5. Kadra

    marek = Zookeeper("Marek")
    anna = Vet("Anna", salary_val=6000.0)

    print("Raport ZOO:")
    print(f"Liczba zwierząt na wybiegu {wybieg_afryka.name}: {len(wybieg_afryka)}")

    koszt_wybiegu = wybieg_afryka.total_maintenance_cost()
    print(f"Całkowity miesięczny koszt karmy na tym wybiegu: {koszt_wybiegu}") 

    print (" Działania personelu:")
    print(marek.perform_duty())
    print(marek.feed_animal(simba.name))
    print(anna.perform_duty())
    print(anna.heal_animal(dumbo.name))

#6. Finanse

    print(f"Łączny koszt wypłat (Marek + Anna): {marek.salary + anna.salary}:")
          
if __name__ == "__main__":
    main()