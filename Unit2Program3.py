# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Base class Employee
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def show_employee(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


# Derived class Manager (inherits from Person and Employee)
class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def show_manager(self):
        self.show_person()
        self.show_employee()
        print("Department:", self.department)


# Create object
m = Manager("Tanishka", 20, "E101", 50000, "HR")

# Display details
m.show_manager()