from func import Simulation, Population, graphics
from tkinter import Tk, Canvas, Entry
from time import sleep


print("Welcome to the Virus Outbreak Simulator\n\n")

input("To start press enter >>> ")


sim = Simulation()

canvas_width = 600
canvas_height = 600

sim_window = Tk()
sim_window.attributes("-topmost", True)
sim_window.title("Epidemic Outbreak")

sim_canvas = Canvas(sim_window, width=canvas_width, height=canvas_height, bg="lightblue")
sim_canvas.grid(padx=(5, 5), pady=(5, 5), row=1, column=0)

info_text = Entry(sim_window)
info_text.grid(row=0, column=0)

pop = Population(sim)

pop.initial_infection(sim)

for day in range(1, sim.simulate_days + 1):
    pop.spread_infection(sim)
    pop.update(sim)
    graphics(sim, pop, sim_canvas)
    info_text.insert(0, f"Day: {day}")
    sim_window.update()
    pop.display_statistics(sim)
    sim.day_number += 1
    sim_window.after(350)
    info_text.delete(0, "end")
    if day != sim.simulate_days-1:
        sim_canvas.delete("all")
