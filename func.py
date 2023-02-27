from random import choice, randint


class InfectionSimulator:
    def __init__(self, contact):
        self.infected = 0
        self.dead = 0
        self.data = []
        self.infect_rate = contact

    def infect(self, input_count):
        for spread in range(int(input_count)):
            while True:
                incident = self.data.index(choice(self.data))
                if not self.data[incident]["infected"]:
                    self.data[incident]["infected"] = True
                    self.infected += 1
                    break

    def rip_check(self, overcome_days, mortality_rate):
        for person_infected in range(len(self.data)):
            if not self.data[person_infected]['dead'] and self.data[person_infected]['infected']:
                if randint(0, 100) > int(mortality_rate):
                    if self.data[person_infected]['days_infected'] < int(overcome_days):
                        self.data[person_infected]['days_infected'] += 1
                        self.spread(person_infected)
                    else:
                        self.data[person_infected]['infected'] = False
                        self.data[person_infected]['was_infected_for'] = self.data[person_infected]['days_infected']
                        self.data[person_infected]['days_infected'] = 0
                        self.infected = self.infected - 1
                else:
                    self.data[person_infected]['dead'] = True
                    self.infected = self.infected - 1
                    self.dead += 1

    def spread(self, infected_person):
        if randint(0, 100) < int(self.infect_rate):
            if randint(1, 2) == 1:
                try:
                    self.data[int(infected_person) + 1]['infected'] = True
                    self.infected += 1
                except IndexError:
                    pass

            else:
                try:
                    self.data[int(infected_person) - 1]['infected'] = True
                    self.infected += 1
                except IndexError:
                    pass

    def create_population(self, input_data):
        for person in range(int(input_data)):
            self.data.append(
                {"person": person, "infected": False, "days_infected": 0, "was_infected_for": 0, "dead": False})
