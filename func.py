from random import choice, randint
from os import system
from time import sleep

class InfectionSimulator:
    def __init__(self, contact, population, infected, overcome, mortality, days):
        self.infected = 0
        self.dead = 0
        self.population_data = []
        self.infect_rate = int(contact)
        self.overcome_days = int(overcome)
        self.mortality_rate = int(mortality)
        self.simulate_days = int(days)
        self.create_population(int(population))
        self.infect(int(infected))
        self.print_daily_news()

    def infect(self, input_count):
        for spread in range(int(input_count)):
            while True:
                incident = self.population_data.index(choice(self.population_data))
                if not self.population_data[incident]["infected"]:
                    self.population_data[incident]["infected"] = True
                    self.infected += 1
                    break

    def rip_check(self, overcome_days, mortality_rate):
        for person_infected in range(len(self.population_data)):
            if not self.population_data[person_infected]['dead'] and self.population_data[person_infected]['infected']:
                if randint(0, 100) > int(mortality_rate):
                    if self.population_data[person_infected]['days_infected'] < int(overcome_days):
                        self.population_data[person_infected]['days_infected'] += 1
                        self.quarantine_person(person_infected)
                        self.spread(person_infected)
                    else:
                        self.population_data[person_infected]['infected'] = False
                        self.population_data[person_infected]['was_infected_for'] = self.population_data[person_infected]['days_infected']
                        self.population_data[person_infected]['days_infected'] = 0
                        self.infected = self.infected - 1
                else:
                    self.population_data[person_infected]['dead'] = True
                    self.infected = self.infected - 1
                    self.dead += 1

    def quarantine_person(self, person_infected):
        if randint(0, 100) < 2:
            self.population_data[int(person_infected)]['is_quarantined'] = True

    def spread(self, infected_person):
        if randint(0, 100) < int(self.infect_rate):
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
        for person in range(int(input_data)):
            self.population_data.append(
                {"person": person, "infected": False, "days_infected": 0, "was_infected_for": 0, "dead": False,
                 "is_quarantined": False})

    def print_daily_news(self):
        for day in range(1, self.simulate_days + 1):
            sleep(0.2)
            system('cls')
            self.rip_check(self.overcome_days, self.mortality_rate)
            print(f"\n-----Day #{day}-----")
            print(f"Percentage of People infected: {(self.infected / len(self.population_data) - self.dead) * 100}%\n")
            print(f"Percentage of people dead: {(self.dead / len(self.population_data)) * 100}%\n")
            print(f"Total people infected: {self.infected}/{len(self.population_data)}\n")
            print(f"Total people dead: {self.dead}/{len(self.population_data)}\n")
            input("\nPress enter to continue >>> ")
