import random 

class questions:
    def __init__(self,name,film,opinion,rating):
        self.name=name
        self.film=film
        self.opinion=opinion
        self.rating=rating

    def people(self):
        print("hello",self.name)
    
    def review(self):
        if rating <1 or rating >10:
            print("rating between 1 and 10")
        else:
            print("review saved")

    def save(self):
        with open ("scores.txt","a") as f:
            f.write(f"reviewer nane: {self.name} movie:{self.film} rating:{self.rating} opinion: {self.opinion}")

    def history(self):
        with open("scores.txt","r") as f:
            print(f.read())

    def delete(self):
        with open("scores.txt","w") as f:
            pass
            print("reviews deleted")

name = input ("enter name:")
film = input("enter movie you want to review:  ")
rating = int(input ("enter a rating between 1 and 10"))
opinion = input ("enter your opinion about the movie:")

show = questions(name,film,opinion,rating)
show.review()
show.save()

while True:
    print("1.review 2.new review 3.view review history 4.delete hisyory 5.quit")
    choice = input("choose option")

    if choice==1:
        show.rewiew()
    elif choice==2:
        show.people
    elif choice == 3:
        show.history()
    elif choice==4:
        show.delete()
    elif choice==5:
        print("goodbye")
        break
    else:
        print("invalid")
    




        
        