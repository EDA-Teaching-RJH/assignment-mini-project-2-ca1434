import random


class questions:
    def __init__(self,name,id):
        self.name=name 
        self.id=id
        self.Mscore=0

    def people(self):
      print("hello",self.name)
  
    def review(self):
       film = input("enter which movie to review: Iron man 1 , Captain America: cival war , avengers endgame:")
       rating = input ("enter a score from 1 to 10:")
       opinion = input ("enter your opinion of the movie:")

       if answer==c:
           print("correct")
           self.score += 1
       else:
           print("wrong it",c)

    def save(self):
        with open ("scores.txt","a") as f:
            f.write(f"student: {self.name} id: {self.id} score: {self.score}")
    
    def history(self):
        with open ("scores.txt","r") as f:
         print(f.read())
    
    def delete(self):
        with open("scores.txt","w") as f:
            pass
            print("deleted")
        
name = input("name")
id = input("Id")

maths = questions(name,id)
maths.student()
maths.save()

while True:
    print("1.test 2.new student 3.view test history 4.delete history 5.quit")
    choice = input("choose option")

    if choice == "1":
      maths.test()
      
    elif choice == "2":
        name = input("name")
        id = input("Id")
        maths.student()
    elif choice == "3":
        maths.history()
    elif choice == "4":
        maths.delete()
    elif choice == "5":
        print("goodbye")
        break
    else:
        print("invalid")
    
    



