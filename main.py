from func import InfectionSimulator


population = input("To simulate virus outbreak Input The population size >>> ")

infected = input("Input the initially infected population size >>> ")

contact = input("Input the percentage of infection rate after contact >>> ")

overcome = input("Input how many days are needed for infection to pass >>> ")

mortality = input("Input the percentage of mortality rate >>> ")

days = input("Input how many days do you want to simulate >>> ")

ground_zero = InfectionSimulator(contact)

ground_zero.create_population(population)

ground_zero.infect(infected)

for day in range(1, int(days)+1):
    ground_zero.rip_check(overcome, mortality)
    print(f"\n-----Day #{day}-----")
    print(f"Percentage of People infected: {(ground_zero.infected/len(ground_zero.data))*100}%\n")
    print(f"Percentage of people dead: {(ground_zero.dead/len(ground_zero.data))*100}%\n")
    print(f"Total people infected: {ground_zero.infected}/{len(ground_zero.data)}\n")
    print(f"Total people dead: {ground_zero.dead}/{len(ground_zero.data)}\n")
    cont_inp = input("\nPress enter to continue >>> ")
