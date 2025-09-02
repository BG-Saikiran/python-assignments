class Hero_Honda():
    company_name = "Hero Honda"  #Class Varaible
    
    def __init__(self,bike_name,bike_model,bike_price):
        self.bike_name = bike_name
        self.bike_model = bike_model
        self.bike_price = bike_price

    def details(self):
        #print("Bike Company",Hero_Honda.company_name) 
        print("Bike Name: ",self.bike_name)      #Instance Method
        print("Bike Model: ",self.bike_model)
        print("Bike Price: ",self.bike_price)

    @classmethod                                 #Class Method
    def changed_Company_name(cls,new_name):
        cls.company_name = new_name
        print("  Company changed to",new_name)

    @staticmethod                                 #Static Method
    def check_cc(cc):
        if cc>= "100cc":
            print(cc)

#    Object1
#print(Hero_Honda.bike_model)                 #Atribute error
passion_pro = Hero_Honda("PassionPro","110cc",70000)
print("Bike Company: ",Hero_Honda.company_name)
passion_pro.colour = "black"                 #Instance Variable
print("Bike Colour: ",passion_pro.colour)
passion_pro.details()
passion_pro.changed_Company_name("Honda Shine")
passion_pro.check_cc(passion_pro.bike_model)



#    Object2
glamour = Hero_Honda("Glamour","125cc",100000)
glamour.colour = "Red"                       #Instance Variable
print("Bike Colour: ",glamour.colour)
glamour.details()
glamour.changed_Company_name("Hero")
