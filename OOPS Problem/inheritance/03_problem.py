# Create a class 'Employee' and add salary and increment properties to it.
# Write a method 'salaryAfterIncrement' method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 1000
    increment = 10
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + ((self.increment * self.salary) / 100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_increment):
        self.increment = new_increment

onkar = Employee()
print("Salary after increment (initial):", onkar.salaryAfterIncrement)

# Change the increment value
onkar.salaryAfterIncrement = 15
print("Salary after increment (after change):", onkar.salaryAfterIncrement)
