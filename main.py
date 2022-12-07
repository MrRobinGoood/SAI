import random
from unit import Unit
from population import Population

# profit
R1 = 1.145284155
R2 = 0.004854395
R3 = 0.01307821
R4 = 0.010720222


def avg_profit_population(population):
    summary = 0
    for i in range(len(population)):
        weights = population[i].get_weights()
        print(weights)
        summary_one = weights[0]/100*R1+weights[1]/100*R2+weights[2]/100*R3+weights[3]/100*R4
        summary += summary_one
        print(summary_one/4)
    return summary/100


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
    for i in range(100):
        test = Population(result)
        test.selection(count_selection)
        result = test.crossing()
        avg_profit_population(result)
        ka = ka + 1
        # for i in range(len(result)):
        #
        #     print(i, " ", result[i].get_weights())


print(ka)
