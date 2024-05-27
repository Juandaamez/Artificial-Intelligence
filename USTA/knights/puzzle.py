# Juan David Amezquita Nuñez
from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A dice "Soy tanto caballero como pícaro."
knowledge0 = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
                 Biconditional(AKnight, And(AKnight, AKnave)))

# Puzzle 1
# A dice "Ambos somos pícaros."
# B no dice nada.
knowledge1 = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
                 Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
                 Biconditional(AKnight, And(AKnave, BKnave)))

# Puzzle 2
# A dice "Somos del mismo tipo."
# B dice "Somos de tipos diferentes."
knowledge2 = And(
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)), Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))))

# Puzzle 3
# A dice "Soy un caballero." o "Soy un pícaro.", pero no sabes cuál.
# B dice "A dijo 'Soy un pícaro'."
# B dice "C es un pícaro."
# C dice "A es un caballero."
knowledge3 = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
                 Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
                 Or(CKnight, CKnave), Not(And(CKnight, CKnave)),
                 Implication(BKnight, And(Not(AKnight), CKnave)),
                 Implication(BKnave, Not(And(Not(AKnight), CKnave))),
                 Implication(CKnight, AKnight),
                 Implication(CKnave, Not(AKnight)))


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [("Puzzle 0", knowledge0), ("Puzzle 1", knowledge1),
               ("Puzzle 2", knowledge2), ("Puzzle 3", knowledge3)]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
