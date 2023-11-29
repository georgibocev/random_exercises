# Task: Define classes for managing employees, including classes for Employee, Manager, Engineer, etc. Implement methods for promotions, demotions, and salary adjustments.
# Example Input: employee.promote()
# Example Output: Promotion successful. New title: Manager

class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
        self.is_engineer = False
        self.is_manager = False

    def adjust_salary(self, new_salary):
        self.salary = new_salary
        return f"Salary adjusted. New salary is: {self.salary}"

    def demote(self):
        if self.is_manager:
            self.is_manager = False
            self.title = "Engineer"
            return f"Demotion successful. {self.name} is now an Engineer."
        elif self.is_engineer:
            self.is_engineer = False
            self.title = "Employee"
            return f"Demotion successful. {self.name} is now an Employee."
        else:
            self.title = "Leaver"
            return "You are kicked out of the company"

    def promote(self):
        if not self.is_engineer:
            self.is_engineer = True
            self.title = "Engineer"
            return f"Promotion successful. New title: {self.title}"
        elif not self.is_manager:
            self.is_manager = True
            self.title = "Manager"
            return f"Promotion successful. New title: {self.title}"
        else:
            return "Already at the highest position."

class Engineer(Employee):
    def __init__(self, name, title, salary):
        super().__init__(name, title, salary)


class Manager(Employee):
    def __init__(self, name, title, salary):
        super().__init__(name, title, salary)



exampleEmp = Employee("Georgi", "Employee", 20000)
print(exampleEmp.title)
print(exampleEmp.promote())
print(exampleEmp.promote())
print(exampleEmp.promote())
print(exampleEmp.demote())
print(exampleEmp.demote())
print(exampleEmp.demote())