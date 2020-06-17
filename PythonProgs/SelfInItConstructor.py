
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


Parin = Employee("Parin", 255, "Instructor")

# Keval = Employee()
# Parin.name = "Parin"
# Parin.salary = 455
# Parin.role = "Instructor"
#
# Keval.name = "Keval"
# Keval.salary = 4554
# Keval.role = "Student"

print(Parin.salary)

