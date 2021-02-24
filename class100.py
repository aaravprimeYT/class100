import random
#from google import google
#num_page = 3
#search_results = google.search("This is my query", num_page)


gameType = ["Adventure", "Racing", "Survival", "Action", "Creative", "Sandbox"]

gameName = ["Minecraft", "Forza", "GTAO", "GTAV", "Roblox"]

class Game():
    def __init__(self,Name,Type,Age,AgeAllowed,Popularity):
        self.Name = Name
        self.Type = Type
        self.Age = Age
        self.AgeAllowed = AgeAllowed
        self.Popularity = Popularity

    #for result in search_results:
            #print(result.description)
    
    def setType(self,Type):
        self.Type = gameType[random.randint(0,5)]

    def findGameName(self,data, word):
        if len(data) == 0:
            return "Not found!"
        else:
            if word in data[0]:
                return word
            else:
                return search(data[1:], word)


Mc = Game("Minecraft", "Sandbox", 12, "10+", "126m")
print(Mc.findGameName(gameName,"Minecraft"))
Mc.AgeAllowed = "18+"
print(Mc.AgeAllowed)
