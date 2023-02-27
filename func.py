from random import choice, randint
from os import system
from time import sleep
from math import sqrt


class InfectionSimulator:
    """Model of infection simulator"""

    def __init__(self):
        self.infected = 0
        self.dead = 0
        self.population_data = []
        bad_input = "Bad Input! only use numeric characters"
        while True:
            try:
                self.population = int(input("To simulate virus outbreak"
                                            " Input The population size >>> "))
                break
            except ValueError:
                print(bad_input)
                sleep(1)
                system('cls')
        while True:
            try:
                self.infected = int(input("Input the initially infected population size >>> "))
                break
            except ValueError:
                print(bad_input)
                sleep(1)
                system('cls')
        while True:
            try:
                self.infect_rate = float(input("Input the percentage of infection "
                                               "rate after contact >>> "))
                break
            except ValueError:
                print(bad_input)
                sleep(1)
                system('cls')
        while True:
            try:
                self.overcome_days = input("Input how many days are "
                                           "needed for infection to pass >>> ")
                break
            except ValueError:
                print(bad_input)
                sleep(1)
                system('cls')
        while True:
            try:
                self.mortality_rate = float(input("Input the percentage "
                                                  "of mortality rate >>> "))
                break
            except ValueError:
                print(bad_input)
                sleep(1)
                system('cls')
        while True:
            try:
                self.simulate_days = int(input("Input how many days do "
                                               "you want to simulate >>> "))
                break
            except ValueError:
                print(bad_input)
                sleep(1)
                system('cls')

        root = sqrt(self.population)
        if int(root + .5) ** 2 != self.population:
            root = round(root, 0)
            self.sqrt_size = int(root)
            self.population = self.sqrt_size ** 2
            print(self.population)
        else:
            self.sqrt_size = int(sqrt(self.population))
        self.create_population(int(self.population))
        self.infect(int(self.infected))
        self.print_daily_news()

    def infect(self, input_count):
        """Initially infects the population"""
        for spread in range(int(input_count)):
            while True:
                incident = self.population_data.index(choice(self.population_data))
                if not self.population_data[incident]["infected"]:
                    self.population_data[incident]["infected"] = True
                    self.infected += 1
                    break

    def rip_check(self, overcome_days, mortality_rate):
        """Checks if person got well or died"""
        for person_infected in range(len(self.population_data)):
            if not self.population_data[person_infected]['dead'] and\
                    self.population_data[person_infected]['infected']:
                if randint(0, 100) > mortality_rate:
                    if self.population_data[person_infected]['days_infected'] < int(overcome_days):
                        self.population_data[person_infected]['days_infected'] += 1
                        self.quarantine_person(person_infected)
                        self.spread(person_infected)
                    else:
                        self.population_data[person_infected]['infected'] = False
                        self.population_data[person_infected]['was_infected_for'] = \
                            self.population_data[person_infected]['days_infected']
                        self.population_data[person_infected]['days_infected'] = 0
                        self.infected = self.infected - 1
                else:
                    self.population_data[person_infected]['dead'] = True
                    self.infected = self.infected - 1
                    self.dead += 1

    def quarantine_person(self, person_infected):
        """Used to quarantine the infected person to stop infection spread"""
        if randint(0, 100) < 2:
            self.population_data[int(person_infected)]['is_quarantined'] = True

    def spread(self, infected_person):
        """Used to determine the spread of infection"""
        if randint(0, 100) < self.infect_rate:
            if not self.population_data[int(infected_person)]['is_quarantined']:
                if randint(1, 2) == 1:
                    try:
                        self.population_data[int(infected_person) + 1]['infected'] = True
                        self.infected += 1
                    except IndexError:
                        pass

                else:
                    try:
                        self.population_data[int(infected_person) - 1]['infected'] = True
                        self.infected += 1
                    except IndexError:
                        pass

    def create_population(self, input_data):
        """Creates instance of population"""
        for person in range(int(input_data)):
            self.population_data.append({
                'person': person,
                'infected': False,
                'days_infected': 0,
                'was_infected_for': 0,
                'dead': False,
                'is_quarantined': False
            })

    def print_daily_news(self):
        """Prints the results of a day"""
        for day in range(1, self.simulate_days + 1):
            sleep(0.2)
            system('cls')
            self.rip_check(self.overcome_days, self.mortality_rate)
            print(f"\n-----Day #{day}-----")
            print(
                f"Percentage of People infected:"
                f" {round((self.infected / (len(self.population_data) - self.dead)) * 100, 2)}%\n")
            print(f"Percentage of people dead: {round((self.dead / len(self.population_data)) * 100, 2)}%\n")
            print(f"Total people infected: {self.infected}/{len(self.population_data)}\n")
            print(f"Total people dead: {self.dead}/{len(self.population_data)}\n")
            input("\nPress enter to continue >>> ")
