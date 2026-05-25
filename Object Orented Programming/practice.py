# Question 1 → Mobile Class

# Create a class Mobile with:

# class variable → shopName
# constructor should take:
# brand
# price
# RAM

# Create 2 objects with different values and print all details.

class Mobile:
    def __init__(self,brand,price,RAM):
        self.brand=brand
        self.price=price
        self.RAM= RAM

       

        

mobile1= Mobile("vivo",78788,"12GB")
print("Brand",mobile1.brand)
print("Price",mobile1.price)
print("RAM",mobile1.RAM)

mobile2= Mobile("apple",67000,"8GB")
print("Brand",mobile2.brand)
print("Price",mobile2.price)
print("RAM",mobile2.RAM)


# Question 2 → Employee Class

# Create a class Employee with:

# class variable → officeName
# constructor should take:
# employeeName
# salary
# department

# Create 2 employees.

class Employee:
    officeName="Google Noida"
    def __init__(self,Name,salary,department):
        self.Name=Name
        self.salary=salary
        self.department=department


Employee1=Employee("Rishi","89000 Rs","Cloud Computing")
print("Office",Employee1.officeName)
print("Employee Name",Employee1.Name)
print("Salary",Employee1.salary)
print("Department",Employee1.department)

Employee2=Employee("Shalu","98000 Rs","Software")
print("Office",Employee2.officeName)
print("Employee Name",Employee2.Name)
print("Salary",Employee2.salary)
print("Department",Employee2.department)
        

# Question 4 → Movie Class

# Create a class Movie.

# Class variable:

# industry = "Hollywood"

# Constructor should take:

# movieName
# rating
# heroName

# Print all movie details.


class Movie:
    industry="Hollywood"
    def __init__(self,movie,rating,heroname):
        self.movie=movie
        self.rating=rating
        self.heroname=heroname

Movie1= Movie("Spiderman Brand New Day","8.9","Peter Parker")
print("Industry-->",Movie1.industry)
print("Movie Name",Movie1.movie)
print("IMDB Rating",Movie1.rating)
print("Hero Name",Movie1.heroname)
        




        
        