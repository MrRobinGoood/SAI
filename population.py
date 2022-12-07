import random
from unit import Unit


def bin_decode(chromosome):
    w1 = int(chromosome[0:7], 2)
    w2 = int(chromosome[7:14], 2)
    w3 = int(chromosome[14:21], 2)
    w4 = int(chromosome[21:28], 2)
    return [w1, w2, w3, w4]

def softmax(weights):
    sumo = sum(weights)
    proportion_weights = [round(weights[0] / sumo,2)*100, round(weights[1] / sumo,2)*100, round(weights[2] / sumo,2)*100, 100 - round(weights[0] / sumo,2)*100 - round(weights[1] / sumo,2)*100 - round(weights[2] / sumo,2)*100]
    if proportion_weights[3]<0:
        proportion_weights[3]=0
    normal_weights = [int(proportion_weights[0]),int(proportion_weights[1]),int(proportion_weights[2]),int(proportion_weights[3])]
    return normal_weights


class Population(object):
    def __init__(self, parents):
        self.population = parents


    def selection(self,selection_count):
        select_population = []
        for i in range(selection_count):
            random_number = random.randint(0, len(self.population) - i - 1)
            select_population.append(self.population[random_number])
            self.population.pop(random_number)
        self.population = select_population

    def mutation(self, chromosome):
        mutating_chromosome = chromosome
        if(random.randint(1,100)==1):
            lucky_num = random.randint(0,27)
            if mutating_chromosome[lucky_num] == '1':
                return mutating_chromosome[:lucky_num] + '0' + mutating_chromosome[lucky_num+1:]
            else:
                return mutating_chromosome[:lucky_num] + '1' + mutating_chromosome[lucky_num+1:]
        return mutating_chromosome




    def crossing(self):
        crossing_population = []
        for i in range(0,len(self.population),2):

            screw = list(self.population[i].get_chromosome())
            screw2 = list(self.population[i+1].get_chromosome())
            # print(screw)
            # print(screw2)
            child1 = []
            child2 = []

            for j in range(2):
                crew = list(self.population[i].get_chromosome())
                crew2 = list(self.population[i+1].get_chromosome())
                a = random.randint(1, 26)
                b = random.randint(1, 27 - a)
                c = 28 - a - b

                child1.clear()
                child2.clear()
                child1.append(crew[:a])
                del crew[:a]

                child2.append(crew2[:a])
                del crew2[:a]

                child1.append(crew2[:b])
                del crew2[:b]

                child2.append(crew[:b])
                del crew[:b]

                child1.append(crew[:c])
                del crew[:c]

                child2.append(crew2[:c])
                del crew2[:c]

                child1_chromosome = ""
                for i in range(3):
                    for j in range(len(child1[i])):
                        child1_chromosome += str(child1[i][j])
                child1_chromosome += str(child1[0][0])

                child2_chromosome = ""
                for i in range(3):
                    for j in range(len(child2[i])):
                        child2_chromosome += str(child2[i][j])
                child2_chromosome += str(child2[0][0])

                crossing_population.append(Unit(softmax(bin_decode(self.mutation(child1_chromosome)))))
                crossing_population.append(Unit(softmax(bin_decode(self.mutation(child2_chromosome)))))

        return crossing_population




