
class Employee:
    no_of_leaves = 8
    pass

Parin = Employee()
Keval = Employee()

Parin.name = "Parin"
Parin.salary = 455
Parin.role = "Instructor"

Keval.name = "Keval"
Keval.salary = 4554
Keval.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)

