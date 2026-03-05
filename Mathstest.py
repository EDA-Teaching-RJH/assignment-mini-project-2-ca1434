import random


class questions:
    def __init__(self,name,id):
        self.name=name 
        self.id=id
        self.score=0

    def student(self):

        print("hello",self.name)
  
    def test(self):
       a = random.randint(1,20)
       b = random.randint(1,20)
       c = a+b

       answer = int(input (f"whats {a} + {b}?"))
       if answer==c:
           print("correct")
           self.score += 1
       else:
           print("wrong it",c)

    def save(self):
        with open ("scores.txt","a") as f:
            f.write(f"student: {self.name} id: {self.id} score: {self.score}/n")
    
    def history(self):
        with open ("scores.txt","r") as f:
         print(f.read())
        
name = input("name")
id = input("Id")

maths = questions(name,id)
maths.student()
maths.test()
maths.save()
maths.history()

while true:
    print("1.test 2.view test history 3.delete history 4.quit")
    choice = input("choose option")

    if choice == 1:
      maths.test()
    elif choice == 2:
        maths.history()
    elif choice == 3:
        maths.delete
    elif choice == 4:
        print("goodbye")
        break
    else:
        print("invalid")
    
    



