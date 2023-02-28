from random import choice, randint
from os import system
from time import sleep
from math import sqrt


class Simulation:
    """Model of infection simulator"""

    def __init__(self):
        self.day_number = 1

        self.population = int(input("To simulate virus outbreak"
                                    " Input The population size >>> "))
        self.initially_infected = float(input("Input initially infected population percentage >>> "))
        self.infect_probability = float(input("Input the percentage of infection rate after contact >>> "))
        self.heal_days = input("Input how many days are needed to heal >>> ")
        self.mortality_percent = float(input("Input the percentage of mortality rate >>> "))
        self.simulate_days = int(input("Input how many days do "
                                       "you want to simulate >>> "))
        root = sqrt(self.population)
        if int(root + .5) ** 2 != self.population:
            root = round(root, 0)
            self.sqrt_size = int(root)
            self.population = self.sqrt_size ** 2
        else:
            self.sqrt_size = int(sqrt(self.population))


class Person:
    """A class model of each person"""

    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.quarantined = False
        self.days_infected = 0

    def infect(self, simulation):
        """Infect a person"""
        if randint(0, 100) < simulation.infect_probability and not self.quarantined:
            self.is_infected = True

    def heal(self):
        """Heal person"""
        self.is_infected = False
        self.days_infected = 0

    def quarantine(self):
        """Quarantine infected person to prevent future infection spread"""
        self.quarantined = True

    def die(self):
        """Kill a person"""
        self.is_dead = True

    def health_check_up(self, simulation):
        """Do a check on a person if he got well or died"""
        if not self.is_dead and self.days_infected:
            self.is_infected += 1
            if randint(0, 100) < 2:
                self.quarantine()
            elif randint(0, 100) < simulation.mortality_percent and not self.quarantined:
                self.die()
            elif self.days_infected == simulation.heal_days:
                self.heal()


class Population:
    """Class model for initial population creation"""

    def __init__(self, simulation):
        self.population_data = []

        for i in range(simulation.sqrt_size):
            row = []
            for b in range(simulation.sqrt_size):
                person = Person()
                row.append(person)
            self.population_data.append(row)

    def initial_infection(self, simulation):
        """Initially infect parts of the population"""
        infected_count = int(round(simulation.initially_infected * simulation.population, 0))

        infections = 0

        while infections < infected_count:
            x_cord = randint(0, simulation.sqrt_size - 1)
            y_cord = randint(0, simulation.sqrt_size - 1)
            if not self.population_data[x_cord][y_cord]:
                self.population_data[x_cord][y_cord].is_infected = True
                self.population_data[x_cord][y_cord].days_infected = 1
                infections += 1

    def update(self, simulation):
        """Update population data by updationg chach individual person"""
        for row in self.population_data:
            for person in row:
                person.health_check_up(simulation)

    def display_statistics(self, simulation):
        """Show the result of each day"""
        total_persons_infected = 0
        total_persons_dead = 0

        for row in self.population_data:
            for person in row:
                if person.is_infected:
                    total_persons_infected += 1
                    if person.is_dead:
                        total_persons_dead += 1

        print(f"\n-----Day #{simulation.day_number}-----")
        print(f"Percentage of People infected:"
              f"{round((total_persons_infected / (len(simulation.population))) * 100, 2)}%\n")
        print(f"Percentage of people dead: "
              f"{round((total_persons_dead / len(simulation.population)) * 100, 2)}%\n")
        print(f"Total people infected: "
              f"{total_persons_infected}/{len(simulation.population)}\n")
        print(f"Total people dead: "
              f"{total_persons_dead}/{len(self.population_data)}\n")
        input("\nPress enter to continue >>> ")
