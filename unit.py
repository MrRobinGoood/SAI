class Unit(object):

    def __init__(self, weights):
        self.w1 = weights[0]
        self.w2 = weights[1]
        self.w3 = weights[2]
        self.w4 = weights[3]
        self.chromosome = self.bin_coding()

    def bin_coding(self):
        s1 = str(bin(self.w1))[2:]
        for i in range(7 - len(s1)):
            s1 = '0' + s1
        s2 = str(bin(self.w2))[2:]
        for i in range(7 - len(s2)):
            s2 = '0' + s2
        s3 = str(bin(self.w3))[2:]
        for i in range(7 - len(s3)):
            s3 = '0' + s3
        s4 = str(bin(self.w4))[2:]
        for i in range(7 - len(s4)):
            s4 = '0' + s4
        return s1 + s2 + s3 + s4

    def get_weights(self):
        return [self.w1, self.w2, self.w3, self.w4]

    def get_chromosome(self):
        return self.chromosome




