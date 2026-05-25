class Vehicle:
    color="blue" 
    petrolorDiesel="petrol"
    mileage="60"

car= Vehicle()

bike= Vehicle()

aeroplane= Vehicle()

print(car.color)
print(bike.color)
print(aeroplane.color)
print(car.mileage)

# q1 create a class car with attrubute brand ="Scorpip"

class Car:
    name="Scorpio"

obj1= Car()

print(obj1.name)

# Create a class Laptop with attributes: brand, RAM, price. Create 2 objects
# # with different values.

class Laptop:
    brand= "Dell"
    RAM= "16GB"
    price=" 750000"

gaming= Laptop()
students= Laptop()

print("Brand Name",gaming.brand)
print("RAM",students.RAM)


# Create a class Laptop with attributes: brand, RAM, price. Create 2 objects
#  with different values.

class Laptop:
    brand= "default"
    RAM= "default 8GB"
    price= "default 1 lakh"

laptop1= Laptop()
laptop1.brand= "Macbook"
laptop1.RAM= "16GB"
print("laptop1 Brand-",laptop1.brand)
print("laptop1 price-",laptop1.price)

laptop2= Laptop()
laptop2.brand="Lenovo"
laptop2.price= 79000
print("laptop2 brand",laptop2.brand)
print("laptop2 price-", laptop2.price)

# Create a class Mobile with attributes: brand, storage, price. Create 2 objects with different values.
class Mobile:
    brand= "default"
    storage= "64GB"
    price= "30000 Rs"

mobile1= Mobile()
mobile1.brand="VivoX300"
mobile1.price= "120000"

print("Brand Name->",mobile1.brand)
print("Price->",mobile1.price)
print('Storage',mobile1.storage)

mobile2=Mobile()
mobile2.brand="OppoK14 Turbo"
mobile2.storage=" 128GB"

print("Brand Name",mobile2.brand)
print("Storage",mobile2.storage)

# Create a class Movie with attributes: name, rating, hero. Create 2 objects with different values.
class Movie:
    Name= "BATMAN "
    rating=" 6.8"
    hero= ""

movie1= Movie()
movie1.Name="The amazing Spiderman"
movie1.rating= " 7.8"
movie1.hero= "Peter Parker"

print("Movie Name",movie1.Name)
print("IMDB Rating",movie1.rating)
print("Hero",movie1.hero)

movie2= Movie()
movie2.hero= "Bruce Wayne"

print("Movie Name",movie2.Name)
print("Hero",movie2.hero)
print("IMDB Rating",movie2.rating)







