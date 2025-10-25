class Team:
    def __init__(self , name , *players):
        self.name = name
        self.players = players

    def __len__(self):
        return len(self.players)


    def __add__(self, other):
        return Team(self.name , self.players + other.players)

    def __str__(self):
        return f"{self.name},{self.players}"

    def __del__(self):
        print(f"{self.name} deleted .")

team1 = Team("barselona" ,  "a" , "b" , "c")
team2 = Team("real madrid" ,  "d" , "f" , "h")

print(team1)
print(team2)
print(len(team1))
print(team1 + team2)

