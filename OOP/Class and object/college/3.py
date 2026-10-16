class student:
    def __init__(self,name,marks,size):
        self.name = name
        self.marks = marks
        self.size = size

    def avg(self):
        return sum(self.marks)/len(self.marks)

    def highest(self):
        # max(self.marks[])
        hmax = 0
        for i in range(0,self.size):
            if hmax < self.marks[i]:
                hmax = self.marks[i]
        return hmax

s1 = student("Himesh",[100,25,63],3)
print(s1.avg())
print(s1.highest())