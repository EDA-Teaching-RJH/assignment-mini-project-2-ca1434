import random


class questions:
    def __init__(self,name,id):
        self.name=name 
        self.id=id
        self.score=0

    def student(self):
        self.n = input("name")
        self.i = input("Id")
        print("hello",self.n)
  
    def test(self):
       a = random.randint(1,20)
       b = random.randint(1,20)
       c = a+b

       answer = input ("whats {a} + {b}?")
       if answer==c:
           print("correct")
           self.score += 1
       else:
           print("wrong it",c)

    def save(self):
        with open ("scores.txt","a") as f:
            f.write("student: {self.n} id:"{self.i} score: {self.score}")
    
    def history(self):
        with open ("scores.txt","r") as f:
         print(f.read())

maths = questions()
maths.save()
maths.history()


   



