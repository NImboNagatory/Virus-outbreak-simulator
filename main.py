from func import Simulation, Population, graphics
from tkinter import Tk, Canvas


print("Welcome to the Virus Outbreak Simulator\n\n")

input("To start press enter >>> ")


sim = Simulation()

canvas_width = 600
canvas_height = 600

sim_window = Tk()
sim_window.title("Epidemic Outbreak")
sim_canvas = Canvas(sim_window, width=canvas_width, height=canvas_height, bg="lightblue")
sim_canvas.grid()

pop = Population(sim)

pop.initial_infection(sim)

for day in range(1, sim.simulate_days + 1):
    pop.spread_infection(sim)
    pop.update(sim)
    pop.display_statistics(sim)
    graphics(sim, pop, sim_canvas)
    sim.day_number += 1
