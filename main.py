import random

#profit
R1 = 1.145284155
R2 = -0.004854395
R3 = 0.01307821
R4 = 0.010720222

class Chromosome(object):
    def __init__(self, w1,w2,w3,w4):
        """Constructor"""
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4

    def get_w1(self):
        return self.w1

    def set_w1(self, input):
        self.w1 = input

    def get_w2(self):
        return self.w2

    def set_w2(self, input):
        self.w2 = input

    def get_w3(self):
        return self.w3

    def set_w3(self, input):
        self.w3 = input

    def get_w4(self):
        return self.w4

    def set_w4(self, input):
        self.w4 = input

def bin_coding(chromosome):

    s1 = str(bin(chromosome.get_w1()))[2:]
    for i in range(7 - len(s1)):
        s1 = '0' + s1
    s2 = str(bin(chromosome.get_w2()))[2:]
    for i in range(7 - len(s2)):
        s2 = '0' + s2
    s3 = str(bin(chromosome.get_w3()))[2:]
    for i in range(7 - len(s3)):
        s3 = '0' + s3
    s4 = str(bin(chromosome.get_w4()))[2:]
    for i in range(7 - len(s4)):
        s4 = '0' + s4
    return s1+s2+s3+s4

def bin_decoding(bin_code_chromosome):

    w1 = int(bin_code_chromosome[0:7], 2)
    w2 = int(bin_code_chromosome[7:14], 2)
    w3 = int(bin_code_chromosome[14:21], 2)
    w4 = int(bin_code_chromosome[21:28], 2)
    return w1,w2,w3,w4

def profit_chromosome(chromosome):
    return chromosome.get_w1()*R1+chromosome.get_w2()*R2+chromosome.get_w3()*R3+chromosome.get_w4()*R4

def create_new_population(count_chromosome):
    population = []
    for i in range(count_chromosome):
        w1 = random.randint(0,100)
        w2 = random.randint(0,100-w1)
        w3 = random.randint(0,100-w1-w2)
        w4 = 100-w1-w2-w3
        population.append(Chromosome(w1,w2,w3,w4))
    return population

def selection(population,select_count):
    select_population = []
    for i in range(select_count):
        random_number = random.randint(0,len(population)-i-1)
        select_population.append(population[random_number])
        population.pop(random_number)
    return select_population

if __name__ == "__main__":
    count_main_population = 10
    main_population = create_new_population(count_main_population)
    print("---MAIN-POPULATION---")
    for i in range(len(main_population)):
        print("Weights: ",main_population[i].get_w1(),main_population[i].get_w2(),main_population[i].get_w3(),main_population[i].get_w4()," Profit: ",
              profit_chromosome(main_population[i]))

    print("\n---SELECT-POPULATION---")
    count_select = 5
    select_population = selection(main_population, count_select)
    for i in range(len(select_population)):
        print("Weights: ",select_population[i].get_w1(),select_population[i].get_w2(),select_population[i].get_w3(),select_population[i].get_w4()," Profit: ",
              profit_chromosome(select_population[i]))




