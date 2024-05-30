class car:  
    def __init__(self,modelname, year):  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
  
c1 = car("Toyota", 2016)  
c1.display()

class Person:
   
    # init method or constructor 
    def __init__(self, name):
        self.name = name
   
    # Sample Method 
    def say_hi(self):
        print(&#39;Hello, my name is&#39;, self.name)
   
p = Person(&#39;Nikhil&#39;)
p.say_hi()class Person:
   
    # init method or constructor 
    def __init__(self, name):
        self.name = name
   
    # Sample Method 
    def say_hi(self):
        print(&#39;Hello, my name is&#39;, self.name)
   
p = Person(&#39;Nikhil&#39;)
p.say_hi()
