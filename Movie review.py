import re 

class questions:
    def __init__(self,user,film,opinion,rating):
        self.user=user
        self.film=film
        self.opinion=opinion
        self.rating=rating

    def check(self):
        if re.search(r"[aa-zA-Z]{2}[0-9]{2}"):
            print("valid")
        else:
            print("not valid")
    
    def review(self):
        if rating <1 or rating >10:
            print("rating between 1 and 10")
        else:
            print("review saved")

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
        user = input("enter username")
        film = input("enter movie you want to review:  ")
        rating = int(input ("enter a rating between 1 and 10"))
        opinion = input ("enter your opinion about the movie:")
       
        show = questions(user,film,opinion,rating)
        show.check()
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
    




        
        