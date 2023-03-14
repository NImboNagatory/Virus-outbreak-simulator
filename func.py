from random import randint
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
        self.days_infected = 0

    def infect(self, simulation):
        """Infect a person"""
        if randint(0, 100) < simulation.infect_probability:
            self.is_infected = True

    def heal(self):
        """Heal person"""
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        """Kill a person"""
        self.is_dead = True

    def health_check_up(self, simulation):
        """Do a check on a person if he got well or died"""
        if not self.is_dead and self.is_infected:
            self.days_infected += 1
            if randint(0, 100) < simulation.mortality_percent:
                self.die()
            elif self.days_infected == simulation.heal_days:
                self.heal()


class Population:
    """Class model for initial population creation"""

    def __init__(self, simulation):
        self.population_data = []

        for i in range(simulation.sqrt_size):
            row = []
            for j in range(simulation.sqrt_size):
                person = Person()
                row.append(person)
            self.population_data.append(row)

    def initial_infection(self, simulation):
        """Initially infect parts of the population"""
        infected_count = int(round((simulation.initially_infected / 100) * simulation.population, 0))

        infections = 0

        while infections < infected_count:
            x_cord = randint(0, simulation.sqrt_size - 1)
            y_cord = randint(0, simulation.sqrt_size - 1)
            if not self.population_data[x_cord][y_cord].is_infected:
                self.population_data[x_cord][y_cord].is_infected = True
                self.population_data[x_cord][y_cord].days_infected = 1
                infections += 1

    def spread_infection(self, simulation):
        """Spread infection in 2d array based on infected persons position.
         the infection can spread above, below, right and left of the infected"""
        for row in range(simulation.sqrt_size):
            for column in range(simulation.sqrt_size):
                if not self.population_data[row][column].is_dead:
                    if row == 0:
                        if column == 0:
                            if self.population_data[row][column + 1].is_infected or \
                                    self.population_data[row + 1][column].is_infected:
                                self.population_data[row][column].infect(simulation)
                        elif column == simulation.sqrt_size - 1:
                            if self.population_data[row][column - 1].is_infected or \
                                    self.population_data[row + 1][column].is_infected:
                                self.population_data[row][column].infect(simulation)
                        else:
                            if self.population_data[row][column - 1].is_infected or \
                                    self.population_data[row][column + 1].is_infected or \
                                    self.population_data[row + 1][column].is_infected:
                                self.population_data[row][column].infect(simulation)
                    elif row == simulation.sqrt_size - 1:
                        if column == 0:
                            if self.population_data[row][column + 1].is_infected or \
                                    self.population_data[row - 1][column].is_infected:
                                self.population_data[row][column].infect(simulation)
                        elif column == simulation.sqrt_size - 1:
                            if self.population_data[row][column - 1].is_infected or \
                                    self.population_data[row - 1][column].is_infected:
                                self.population_data[row][column].infect(simulation)
                        else:
                            if self.population_data[row][column - 1].is_infected or \
                                    self.population_data[row][column + 1].is_infected or \
                                    self.population_data[row - 1][column].is_infected:
                                self.population_data[row][column].infect(simulation)
                    else:
                        if column == 0:
                            if self.population_data[row][column + 1].is_infected or \
                                    self.population_data[row + 1][column].is_infected or \
                                    self.population_data[row - 1][column].is_infected:
                                self.population_data[row][column].infect(simulation)
                        elif column == simulation.sqrt_size - 1:
                            if self.population_data[row][column - 1].is_infected or \
                                    self.population_data[row + 1][column].is_infected or \
                                    self.population_data[row - 1][column].is_infected:
                                self.population_data[row][column].infect(simulation)
                        else:
                            if self.population_data[row][column - 1].is_infected or \
                                    self.population_data[row][column + 1].is_infected or \
                                    self.population_data[row + 1][column].is_infected or \
                                    self.population_data[row - 1][column].is_infected:
                                self.population_data[row][column].infect(simulation)

    def update(self, simulation):
        """Update population data by checking individual person"""
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
              f"{round((total_persons_infected / simulation.population) * 100, 2)}%\n")
        print(f"Percentage of people dead: "
              f"{round((total_persons_dead / simulation.population) * 100, 2)}%\n")
        print(f"Total people infected: "
              f"{total_persons_infected}/{simulation.population}\n")
        print(f"Total people dead: "
              f"{total_persons_dead}/{simulation.population}\n")


def graphics(simulation, population, canvas):
    """A helper function to display infection spreading amongst population using tkinter canvas"""
    print("i ran")
    square_dim = 600 // simulation.sqrt_size
    for row in range(simulation.sqrt_size):
        y_cord = row * square_dim
        for column in range(simulation.sqrt_size):
            x_cord = column * square_dim
            if population.population_data[row][column].is_dead:
                canvas.create_rectangle(x_cord, y_cord, x_cord + square_dim, y_cord + square_dim, fill="red")
            else:
                if population.population_data[row][column].is_infected:
                    canvas.create_rectangle(x_cord, y_cord, x_cord + square_dim, y_cord + square_dim, fill="yellow")
                else:
                    canvas.create_rectangle(x_cord, y_cord, x_cord + square_dim, y_cord + square_dim, fill="green")
