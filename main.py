class Employee:
    _total_employees = 0
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self._salary = 0
        Employee._total_employees += 1

    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}"
    def set_salary(self, amount):
        self._salary = amount

    @staticmethod
    def total_employees():
        return Employee._total_employees

class Manager(Employee):
    def get_info(self):
        return f"Manager: {self.name}"

    def assign_task(self, task):
        print(f"{self.name} assigns task: {task}")

class SkillMixin:
    def __init__(self):
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)

class Developer(Employee, SkillMixin):
    def __init__(self, name, position):
        Employee.__init__(self, name, position)
        SkillMixin.__init__(self)
    def code(self):
        print(f"{self.name} writes code.")
    def get_info(self):
        skills = ', '.join(self.skills)
        return f"Developer: {self.name}, Skills: {skills}"

manager = Manager("Olexander", "Project Manager")
developer = Developer("Maria", "Programmer")

manager.set_salary(30000)
developer.set_salary(20000)

manager.assign_task("Develop a new module")
developer.add_skill("Python")
developer.add_skill("Django")
developer.code()
for employee in [manager, developer]:
    print(employee.get_info())
print(f"Total number of employees: {Employee.total_employees()}")
