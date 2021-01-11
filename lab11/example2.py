class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary
  def get_name(self):
    return self.name
  def set_name(self,name):
    self.name = name
  def get_salary(self):
    return self.salary
  def set_salary(self,salary):
    if salary > 0 :
      self.salary = salary
  def display(self):
    print("Name:" + str(self.name))
    print("Salary:" + str(self.salary))
e1 = Employee(name = "ahmet", salary = 1000)
e2 = Employee(name = "mehmet", salary = 2000)
e3 = Employee(name = "hüseyin",salary = 3000)

class Company:
  def __init__(self):
    self.emlpoyeelist = []
  def get_employee(self):
    return self.employeelist