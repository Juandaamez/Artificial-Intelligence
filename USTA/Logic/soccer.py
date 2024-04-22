from logic import *

players = ["Diaz", "Lautaro", "Kane", "Valverde"]
teams = ["Bayern", "Madrid", "Liverpool", "Inter"]

symbols = list()
KB = And()

# Player and teams
for player in players:
    for team in teams:
        symbols.append(Symbol(f"{player}{team}"))

# Each player belongs to a team
for player in players:
    KB.add(
        Or(
            Symbol(f"{player}Bayern"),
            Symbol(f"{player}Madrid"),
            Symbol(f"{player}Liverpool"),
            Symbol(f"{player}Inter"),
        ))

# Only one player per team
for team in teams:
    for p1 in players:
        for p2 in players:
            if p1 != p2:
                KB.add(
                    Implication(Symbol(f"{p1}{team}"),
                                Not(Symbol(f"{p2}{team}"))))

# Only one team per player
for player in players:
    for t1 in teams:
        for t2 in teams:
            if t1 != t2:
                KB.add(
                    Implication(Symbol(f"{t1}{player}"),
                                Not(Symbol(f"{t2}{player}"))))
                


print(KB.formula())
