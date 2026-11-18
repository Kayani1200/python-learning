class Car:
   def __init__(self, brand,color,model):
     self.brand = brand
     self.color = color
     self.model = model

car1 = Car("Toyota","black","2003")
car2 = Car("Honda","blue","2004")
car3 = Car ("BMW","white","2007")

print(car1.brand,car1.color,car1.model)
print(car2.brand,car2.color,car2.model)
print(car3.brand,car3.color,car3.model)