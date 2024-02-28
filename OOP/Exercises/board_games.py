class Game:
    def __init__(self, name, result):
        self.name = name
        self.result = result
        self.players = []
        self.winners = []
        self.losers = []
        self.most = 0
        self.played = 0
        self.record = 0
        self.record_holder = None
        
    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)
            
    def record_handler(self, player, points):
        if points > self.record:
            self.record = points
            self.record_holder = player
            
    def add_winner(self, player):
        self.winners.append(player.name)
    
    def add_loser(self, player):
        self.losers.append(player.name)
            
    def add_play(self, players):
        self.played += 1
        if len(players) > self.most:
            self.most = len(players)

class Player:
    def __init__(self, name, result):
        self.name = name
        self.result = result
        self.games = []
        self.played = {}
        self.games_won = 0
        self.games_lost = 0
        
    def add_game(self, game):
        if game not in self.games:
            self.played[game] = 0
            self.games.append(game) 
        self.played[game] += 1
            
    def add_win(self):
        self.games_won += 1
        
    def add_loss(self):
        self.games_lost += 1

class Statistics:
    def __init__(self, filename):
        self.games = {}
        self.players = {}
        self.played = 0
        self.lines = open(filename, "r").readlines()
        
        for line in self.lines:
            items = line.strip().split(";")
            players = items[1].split(",")
            results = items[3].split(",")
            game = items[0]
            result = items[2]
            
            if game not in self.games:
                self.games[game] = Game(game, result)
                
            NewGame = self.games[game]
            NewGame.add_play(players)
            
            for player in players:
                if player not in self.players:
                    NewPlayer = Player(player, result)
                    NewPlayer.add_game(NewGame)
                    self.players[player] = NewPlayer
                    NewGame.add_player(NewPlayer)
                else:
                    self.players[player].add_game(NewGame)
                    NewGame.add_player(self.players[player])
                        
            if result == "winner":
                player = self.players[results[0]]
                player.add_win()
                NewGame.add_winner(player)
            elif result == "places":
                for i in results:
                    if results.index(i) == 0:
                        self.players[i].add_win()
                        NewGame.add_winner(self.players[i])
                    elif results.index(i) == len(results)-1:
                        self.players[i].add_loss()
                        NewGame.add_loser(self.players[i])
            elif result == "points":
                unsorted = []
                for i in players:
                    unsorted.append([i, int(results[players.index(i)])])
                sortedlist = []
                for i in sorted(unsorted, key= lambda elem : elem[1]*-1):
                    sortedlist.append(i[0])
                for i in sortedlist:
                    if sortedlist.index(i) == 0:
                        self.players[i].add_win()
                        NewGame.add_winner(self.players[i])
                        NewGame.record_handler(self.players[i].name, int(results[players.index(i)]))
                    elif sortedlist.index(i) == len(sortedlist)-1:
                        self.players[i].add_loss()
                        NewGame.add_loser(self.players[i])
        
                        
    def get(self, path: str):
        args = path.split("/")
        args.pop(0)
        
        if args[0] == "players":
            return list(self.players.keys())
        elif args[0] == "games":
            return list(self.games.keys())
        elif args[0] == "total":
            if len(args) >= 2:
                result = args[1]
                cur = 0
                for game in self.games.values():
                    if game.result == result:
                        cur += game.played
                return cur
            else:
                return len(self.lines)
        elif args[0] == "player":
            player = self.players[args[1]]
            if args[2] == "amount":
                return sum(player.played.values())
            elif args[2] == "favourite":
                fav = None
                diff = 0
                for i in player.played:
                    if player.played[i] > diff:
                        fav = i
                        diff = player.played[i]
                return fav.name
            elif args[2] == "won":
                return player.games_won
        elif args[0] == "game":
            game = self.games[args[1]]
            if args[2] == "amount":
                return game.played
            elif args[2] == "player-amount":
                return game.most
            elif args[2] == "most-wins":
                won = None
                diff = 0
                for i in sorted(game.winners):
                    if game.winners.count(i) > diff:
                        won = i
                        diff = game.winners.count(i)
                return won
            elif args[2] == "most-frequent-winner":
                unsorted = []
                for player in game.players:
                    unsorted.append([player.name, (player.games_won/len(player.played), player.played)])
                sortedlist = []
                for i in sorted(unsorted, key= lambda elem : (elem[1]*-1)):
                    sortedlist.append(i[0])
                return sortedlist[0]
            elif args[2] == "most-losses":
                won = None
                diff = 0
                for i in sorted(game.losers):
                    if game.losers.count(i) > diff:
                        won = i
                        diff = game.losers.count(i)
                return won
            elif args[2] == "most-frequent-loser":
                unsorted = []
                for player in game.players:
                    unsorted.append([player.name, (player.games_lost/len(player.played))])
                sortedlist = []
                for i in sorted(unsorted, key= lambda elem : elem[1]*-1):
                    sortedlist.append(i[0])
                return sortedlist[0]
            elif args[2] == "record-holder":
                return game.record_holder
        else:
            return None
        
lol = Statistics("players.txt")
print(lol.get("/game/terraforming mars/record-holder"))