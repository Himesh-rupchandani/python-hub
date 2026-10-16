# Normal class example

class car():
    # mehod
    def value(self,name,price):
        self.name = name
        self.price = price

        print(self.name,self.price)

car1 = car()
car1.value("BMW",10000000)

car2 = car()
car2.value("Audi",950000)