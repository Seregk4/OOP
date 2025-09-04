class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def get_info(self):
        print(f"Имя: {self.name}\nДолжность: {self.position}\nЗП: {self.salary}")

class Developer(Employee):
    def __init__(self, name, position, salary, programming_language):
        super().__init__(name, position, salary)
        self.programming_language = programming_language
    
    def get_info(self):
        print(f"Имя: {self.name}\nДолжность: {self.position}\nЗП: {self.salary}\nЯП: {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, position, salary,  list_employees : list):
        super().__init__(name, position, salary)
        self.list_employees = list_employees

    def get_info(self):
        super().get_info()
        print("Подчинённые:")
        for emp in self.list_employees:
            print(f"-{emp.name}")

emp1 = Developer("Ivan", "DEV", "100000", "Python")
emp1.get_info()


team_list = [emp1]
mang = Manager("Jhon", "Mang", "1111", team_list)

mang.get_info()

