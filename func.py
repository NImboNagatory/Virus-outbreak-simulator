from random import choice, randint


class InfectionSimulator:
    def __init__(self):
        self.infected = 0
        self.dead = 0
        self.data = []

    def infect(self, input_count):
        for spread in range(int(input_count)):
            while True:
                incident = self.data.index(choice(self.data))
                if not self.data[incident]["infected"]:
                    self.data[incident]["infected"] = True
                    self.infected += 1
                    break

    def rip_check(self, input_data, overcome_days, mortality_rate):
        for person_infected in range(len(input_data)):
            if not input_data[person_infected]['dead'] and input_data[person_infected]['infected']:
                if randint(0, 100) > int(mortality_rate):
                    if input_data[person_infected]['days_infected'] < int(overcome_days):
                        input_data[person_infected]['days_infected'] += 1
                    else:
                        input_data[person_infected]['infected'] = False
                        input_data[person_infected]['was_infected_for'] = input_data[person_infected]['days_infected']
                        input_data[person_infected]['days_infected'] = 0
                        self.infected = self.infected - 1
                else:
                    input_data[person_infected]['dead'] = True
                    self.infected = self.infected - 1
            if input_data[person_infected]['dead']:
                self.dead += 1

    def spread(self, contact_spread):
        if randint(0, 100) > int(contact_spread):
            self.infected += 1

    def create_population(self, input_data):

        for person in range(int(input_data)):
            self.data.append(
                {"person": person, "infected": False, "days_infected": 0, "was_infected_for": 0, "dead": False})
