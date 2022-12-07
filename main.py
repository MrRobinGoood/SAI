import random
from unit import Unit
from population import Population

# profit
R1 = 1.145284155
R2 = 0.004854395
R3 = 0.01307821
R4 = 0.010720222


# def profit_population(population):
#     for i in range(len(population)):
#         population[i].

def start_population(count_units):
    population = []
    for i in range(count_units):
        w1 = random.randint(0, 100)
        w2 = random.randint(0, 100 - w1)
        w3 = random.randint(0, 100 - w1 - w2)
        w4 = 100 - w1 - w2 - w3
        population.append(Unit([w1, w2, w3, w4]))
    return population


# def step_population(population):


if __name__ == "__main__":
    count_units = 100
    count_selection = 50

    test = Population(start_population(count_units))
    test.selection(count_selection)
    result = test.crossing()
    ka = 0
    for i in range(50):
        test = Population(result)
        test.selection(count_selection)
        result = test.crossing()
        ka = ka + 1
        for i in range(len(result)):

            print(i, " ", result[i].get_weights())


print(ka)
