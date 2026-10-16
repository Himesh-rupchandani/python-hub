class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

s1 = student("Himesh",[100,50,30])
print(s1.calculate_average())

s2 = student("Himesh",[100,40,60])
print(s2.calculate_average())

s3 = student("vishal",[50,40,100])
print(s3.calculate_average())