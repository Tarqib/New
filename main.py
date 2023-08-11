print("name")
print("hi")
class person:


    def __init__(self,name,age,gender):
         #constructor define
         self.name = name
         self.age = age
         self.gender = gender
         self.__pwd = "Azim" #private variable declaration#(encapsulation)

    def display(self):
        print(self.name, self.age, self.gender, end="")
    def grow(self):
         self.age +=1
         print(self.age)
#object

#inheritance
class Student(person):
    def __init__ (self,name,age,gender,id,Cgpa):
        self.id = id
        self.Cgpa = Cgpa
        #person.__init__(self,name,age,gender)
        super().__init__(name,age,gender)
    def display(self):
        super().display()
        print(self.id,self.Cgpa)
student = Student("Abir",25,"Male", "111",3.5)
student.display()
#print(person.name)
print(person._person__pwd)#object calling# _ before class, and first person is variable