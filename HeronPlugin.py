import math

class HeronPlugin:
    def input(self, inputfile):
        infile = open(inputfile, 'r')
        self.a = float(infile.readline())
        self.b = float(infile.readline())
        self.c = float(infile.readline())

    def run(self):
        s = (self.a + self.b + self.c) / 2
        self.area = math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def output(self, outputfile):
        print(self.area)

#a = 4.503
#b = 2.377
#c = 3.902
#s = (a + b + c) / 2
#area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#print(area)
