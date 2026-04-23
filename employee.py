class Employee:
    def __init__(self,name,id,email):
        self.name=name
        self.id=id
        self.__email=email

    def decribe(self):
        print(f"{self.name} ,{self.id}")

emply1=Employee("Rita Gadlela",34234,"lod@gmail.com")
emply1.decribe()
