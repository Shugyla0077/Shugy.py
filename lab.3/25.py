class Student:
    def __init__ (self,name,age):

        self.name=name
        self.age=age
    def introduce (self):
        return f"My name is{self.name} and i am{self.age}"
student1=Student("Shugyla", 18)
print(student1.introduce())