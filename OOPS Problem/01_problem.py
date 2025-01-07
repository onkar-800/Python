# Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:

    company = "Mocrosoft" 
    name = "Onkar"   
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    
    def getInfo(self):
        print(f"Enployee name is {self.name}\nEmployee salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")

onkar = Programmer("Onkar",1500000)
onkar.getInfo()
onkar.greet()