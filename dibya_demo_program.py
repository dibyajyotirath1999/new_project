class man:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def nature(self):
        print(self.name,"is a good guy")
        print(self.name,"'s age is",self.age)
class employee(man):
    def __init__(self,name,age,enum,esal,ecom):
        super().__init__(name,age)
        self.enum=enum
        self.esal=esal
        self.ecom=ecom
    def work(self):
        super().nature()
        print("employee number is:",self.enum)
        print("employee salary is:",self.esal)
        print("company name :",self.ecom)
class son(man,employee):
    def __init__(self,name,age,cast,fname,mname):
        man.__init__(name,age)
        self.cast=cast
        self.fname=fname
    def sonbio(self):
        employee.work()
        print("cast is :",self.cast)
        print("father's name:",self.fname)
        print("mother's name:",self.mname)

s=son("dibya",22,"general","manamohan rath","anima rath")
s.sonbio()
print("my name is dibyajyoti rath")
print("i am a softwere aspirant")





        

