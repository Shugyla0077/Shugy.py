class MyClass:
   
    def getString(self):
        self.input_string = input("Enter a string: ")
    
    
    def printString(self):
        print(self.input_string.upper())


my_obj = MyClass()
my_obj.getString()  
my_obj.printString()  