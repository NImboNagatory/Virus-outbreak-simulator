from random import choice, randint
from os import system
from time import sleep
from math import sqrt


class InfectionSimulator:
    """Model of infection simulator"""

    def __init__(self):
        self.population = int(input("To simulate virus outbreak"
                                    " Input The population size >>> "))
        self.initially_infected = int(input("Input initially infected population size >>> "))
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

    # def infect(self, simulation):
    #     """Initially infects the population"""
    #     for spread in range(int(simulation.initially_infected)):
    #         while True:
    #             incident = self.population_data.index(choice(self.population_data))
    #             if not self.population_data[incident]["infected"]:
    #                 self.population_data[incident]["infected"] = True
    #                 self.infected += 1
    #                 break

    # def rip_check(self, overcome_days, mortality_rate):
    #     """Checks if person got well or died"""
    #     for person_infected in range(len(self.population_data)):
    #         if not self.population_data[person_infected]['dead'] and \
    #                 self.population_data[person_infected]['infected']:
    #             if randint(0, 100) > mortality_rate:
    #                 if self.population_data[person_infected]['days_infected'] < int(overcome_days):
    #                     self.population_data[person_infected]['days_infected'] += 1
    #                     self.quarantine_person(person_infected)
    #                     self.spread(person_infected)
    #                 else:
    #                     self.population_data[person_infected]['infected'] = False
    #                     self.population_data[person_infected]['was_infected_for'] = \
    #                         self.population_data[person_infected]['days_infected']
    #                     self.population_data[person_infected]['days_infected'] = 0
    #                     self.infected = self.infected - 1
    #             else:
    #                 self.population_data[person_infected]['dead'] = True
    #                 self.infected = self.infected - 1
    #                 self.dead += 1
    #
    # def quarantine_person(self, person_infected):
    #     """Used to quarantine the infected person to stop infection spread"""
    #     if randint(0, 100) < 2:
    #         self.population_data[int(person_infected)]['is_quarantined'] = True
    #
    # def spread(self, infected_person):
    #     """Used to determine the spread of infection"""
    #     if randint(0, 100) < self.infect_rate:
    #         if not self.population_data[int(infected_person)]['is_quarantined']:
    #             if randint(1, 2) == 1:
    #                 try:
    #                     self.population_data[int(infected_person) + 1]['infected'] = True
    #                     self.infected += 1
    #                 except IndexError:
    #                     pass
    #
    #             else:
    #                 try:
    #                     self.population_data[int(infected_person) - 1]['infected'] = True
    #                     self.infected += 1
    #                 except IndexError:
    #                     pass
    #
    # def create_population(self, input_data):
    #     """Creates instance of population"""
    #     for person in range(int(input_data)):
    #         self.population_data.append({
    #             'person': person,
    #             'infected': False,
    #             'days_infected': 0,
    #             'was_infected_for': 0,
    #             'dead': False,
    #             'is_quarantined': False
    #         })
    #
    # def print_daily_news(self):
    #     """Prints the results of a day"""
    #     for day in range(1, self.simulate_days + 1):
    #         sleep(0.2)
    #         system('cls')
    #         self.rip_check(self.overcome_days, self.mortality_rate)
    #         print(f"\n-----Day #{day}-----")
    #         print(
    #             f"Percentage of People infected:"
    #             f" {round((self.infected / (len(self.population_data) - self.dead)) * 100, 2)}%\n")
    #         print(f"Percentage of people dead: {round((self.dead / len(self.population_data)) * 100, 2)}%\n")
    #         print(f"Total people infected: {self.infected}/{len(self.population_data)}\n")
    #         print(f"Total people dead: {self.dead}/{len(self.population_data)}\n")
    #         input("\nPress enter to continue >>> ")
    #


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
