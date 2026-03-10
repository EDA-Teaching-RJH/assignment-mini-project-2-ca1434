import random 

class questions:
    def __init__(self,name,film,opinion)
        self.name=name
        self.film=film
        self.opinion=opinion

    def people(self):
        print("hello",self.name)
    
    def review(self):
        film = input("enter movie you want to review:  ")
        rating = input ("enter a rating between 1 and 10")
        opinion = input ("enter your opinion about the movie:")

        if rating <1 or >10:
            print("rating between 1 and 10")
        else:
            print("review saved")

    def save(self):
        with open ("scores.txt","a") as f:
            f.write(f"reviewer nane: {self.name} movie:{self.film} rating:{self.rating} opinion: {self.opinion}")

    



        
        