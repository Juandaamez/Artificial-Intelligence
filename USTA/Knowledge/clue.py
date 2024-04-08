from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPluf")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons

def check_knowledge(KB):
    for symbol in symbols:
        if model_check(KB, symbol):
            print(f"{symbol}: YES")
        elif not model_check(KB, Not(symbol)):
            print(f"{symbol}: MAYBE")

KB = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench),
)

KB.add(Not(plum))
KB.add(Or(Not(mustard), Not(library), Not(revolver)))   
check_knowledge(KB)
