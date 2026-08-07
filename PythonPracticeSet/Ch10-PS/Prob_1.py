class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

p = programmer("rajesh", 110000, "5 years")
print(p.name, p.salary, p.experience, p.company)
r = programmer("shubham", 150000, " 3 years")
print(r.name, r.salary, r.experience, r.company)
   