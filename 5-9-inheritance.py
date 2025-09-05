class Vehical:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(self.brand,self.model) 

class Car(Vehical):

    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats = seats

       

    def display_info(self):
        super().display_info()
        print("having",self.seats,"no.of seats")

v1 = Vehical("TATA",2020) 
c1 = Car("Benz",2010,4)  

v1.display_info() 
c1.display_info()       

class Animals:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

class Dog(Animals):
    def __init__(self, name,bread):
        super().__init__(name)
        self.bread = bread
        print(self.bread)

    def describe(self):
        print(f'{self.name} is a {self.bread} Bread')    

class Cat(Dog):
    def __init__(self, name, bread,colour):
        super().__init__(name, bread)
        self.colour = colour

    def describe(self):
        super().describe()  
        print(self.name,"is",self.colour,"coloured")
      
        
dog = Dog("scooby","golden")
cat = Cat("kitti","mora","Orange")
dog.eat()
cat.sleep()
dog.describe()
cat.describe()



                   
