import re 

class questions:
    def __init__(self,user,film,opinion,rating):
        self.user=user
        self.film=film
        self.opinion=opinion
        self.rating=rating
    
    def review(self):
        while True:
         if self.rating >=1 and self.rating <=10:
              print("review saved")
              break   
         else:
             print("rating between 1 and 10")
             self.rating = int(input ("enter a rating between 1 and 10"))
           

    def save(self):
        with open ("scores.txt","a") as f:
            f.write(f"reviewer nane: {self.user} movie:{self.film} rating:{self.rating} opinion: {self.opinion}")

    def history(self):
        with open("scores.txt","r") as f:
            print(f.read())

    def delete(self):
        with open("scores.txt","w") as f:
            pass
            print("reviews deleted")


while True:
    print("hello")
    print("1.new review \n2.view review history \n3.delete history \n4.quit")
    choice = input("choose option")

    if choice=="1":
        while True:
         user = input("enter username")
         if re.search(r"[a-zA-Z]{2}[0-9]{2}",user):
            print("valid")
            break
         else:
            print("not valid")

        film = input("enter movie you want to review:  ")
        rating = int(input ("enter a rating between 1 and 10"))
        
        while True:
         opinion = input ("enter your opinion about the movie:")
         if re.search(r"[a-zA-Z]",user):
            break
         else:
            print("opinion cant be empty")
       
        show = questions(user,film,opinion,rating)
        show.review()
        show.save()
    
    elif choice == "2":
        show.history()
    elif choice=="3":
        show.delete()
    elif choice=="4":
        print("goodbye")
        break
    else:
        print("invalid")
    




        
        