from func import InfectionSimulator
from os import system
from time import sleep

print("Welcome to the Virus Outbreak Simulator\n\n")

input("To start press enter >>> ")

sleep(1)
system('cls')

bad_input = "Bad Input! only use numeric characters"

while True:
    try:
        population = int(input("To simulate virus outbreak Input The population size >>> "))
        break
    except ValueError:
        print(bad_input)
        sleep(1)
        system('cls')
while True:
    try:
        infected = int(input("Input the initially infected population size >>> "))
        break
    except ValueError:
        print(bad_input)
        sleep(1)
        system('cls')
while True:
    try:
        contact = input("Input the percentage of infection rate after contact >>> ")
        break
    except ValueError:
        print(bad_input)
        sleep(1)
        system('cls')
while True:
    try:
        overcome = input("Input how many days are needed for infection to pass >>> ")
        break
    except ValueError:
        print(bad_input)
        sleep(1)
        system('cls')
while True:
    try:
        mortality = input("Input the percentage of mortality rate >>> ")
        break
    except ValueError:
        print(bad_input)
        sleep(1)
        system('cls')
while True:
    try:
        days = input("Input how many days do you want to simulate >>> ")
        break
    except ValueError:
        print(bad_input)
        sleep(1)
        system('cls')

InfectionSimulator(contact, population, infected, overcome, mortality, days)
