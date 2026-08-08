class Employee:
    salary = 764
    increment = 25

    @property
    def salaryAftreIncrement(self):
        return(self.salary + self.salary * (self.increment/100))

    @salaryAftreIncrement.setter
    def salaryAftreIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100


e = Employee()
print(e.salaryAftreIncrement)
e.salaryAftreIncrement = 955.0
print(e.increment)