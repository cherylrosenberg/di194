# https://colab.research.google.com/drive/1B2x_hwTcg70cUAF2IXu25FOyvvXyIdHB?usp=sharing#scrollTo=cell-0017

# IS-A means inheritance. For example, a dog IS A animal, so it inherits its attributes
# HAS-A means composition. For example, a student HAS A classroom. It doesn't inherit the attributes of a classroom
# composition is one class storing references to instances of another class. A Family stores a list of Person objects. A Playlist has a list of Student objects. The objects in the list are fully functional objects with their own attributes and methods. 
# This is how most OOP works in practice. Classes talk to each other

class Player: 
    def __init__(self, name, goals, assists):
        self.name = name
        self.goals = goals
        self.assists = assists

    def stats(self):
        print(f"{self.name}: {self.goals}g / {self.assists}a")

class Team:
    def __init__(self, name):
        self.name = name
        self.players = [] # will hold Player objects

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)

    def total_goals(self):
        return sum(p.goals for p in self.players) # calls each Player's .goals attribute
    
    def top_scorer(self):
        return max(self.players, key=lambda p: p.goals)
        # lambda p: p.goals # given a player p, give me p.goals()

    ## an alternative version without the lambda
    # def top_scorer(self): 
    #     def get_score(p: Player):
    #         return p.goals
    #     return max(self.players, key=get_score)

    def squad_report(self):
        for player in self.players:
            player.stats()
        print(f" Total goals: :{self.total_goals()}")
        best = self.top_scorer()
        print(f" Top Scorer: {best.name} ({best.goals} goals)")

barca = Team("Barcelona")
barca.add_player(Player("Messi", 30, 15))
barca.add_player(Player("Xavi", 12, 20))
barca.add_player(Player("Iniesta", 10, 18))

barca.squad_report()