import random


class questions:
    def __init__(self,name,id):
        self.name=name 
        self.id=id

    def student(self):
        self.n = input("name")
        self.i = input("Id")
        print("hello",self.n)
  
    def test(self):
       a = random.randint(1,20)
       b = random.randint(1,20)
       c = a+b

       answer = input ("enter answer")
       if answer==c:
           print("correct")
       else:
           print("wrong it",c)

    def save(self):
        with open ("scores.txt","a") as f:
            f.write("student:",self.n, "id:",self.i,"score:",c)


   



