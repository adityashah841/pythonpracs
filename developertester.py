class Employee:
    def __init__(self,id,name,Type):
        self.id = id
        self.name = name
        self.Type = Type
    

class Manager(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, Type="Manger")
        self.MangerID = 100*id+id
        self.testers=[]
        self.developers=[]
    
    def add_tester(self,id):
        self.testers.append(id)
    def remove_tester(self,id):
        self.testers.remove(id)

    def add_developer(self,id):
        self.developers.append(id)
    def remove_developer(self,id):
        self.developers.remove(id)

class Tester(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, Type="Tester")
        self.TesterID = 100*id+id
class Developer(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, Type="Developer")
        self.DeveloperID = 100*id+id

m1 = Manager(1,"Rohan")
m2 = Manager(1,"Raj")
t1 = Tester(2,"Tester1")
t2 = Tester(3,"Tester2")
d1 = Developer(4,"dev")

m1.add_developer(d1.id)
m1.add_tester(t1.id)
m2.add_tester(t2.id)

print(f"For Manger 1:\nTester:{m1.testers}\nDevelopers:{m1.developers}")
print(f"For Manger 2:\nTester:{m2.testers}\nDevelopers:{m2.developers}")
