class student:
    def __init__(self,name,roll_number,division):
        self.name = name
        self.roll_number = roll_number
        self.division = division

        print(self.name,self.roll_number,self.division)

student1 = student("Himesh",92500110005,"3EU-1")
print(student1.name)
print(student1.roll_number)
print(type(student1.roll_number))