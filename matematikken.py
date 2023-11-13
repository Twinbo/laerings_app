import random

print("start")
print()

# random number 1
random_number = random.randint(1, 20)
print("første nummer =", random_number)

# random number 2
random_number2 = random.randint(1, 20)
print("anden nummer =", random_number2)

print()

# math thing

# +
class Plus:
    def __init__(self, range_start, range_end):
        self.range_start = range_start
        self.range_end = range_end
        self.random_number = random.randint(range_start, range_end)
        self.random_number2 = random.randint(range_start, range_end)

    def plus_learner(self):
        print("Plus stykke", self.random_number, "+", self.random_number2)
        user_answer = int(input())
        if user_answer == self.random_number + self.random_number2:
            print("Det er rigtigt, Godt gået")
        else:
            print("Prøv igen")
            user_answer = int(input())
            if user_answer == self.random_number + self.random_number2:
                print("Det er rigtigt, godt gået")
            else:
                print("Svaret er forkert, det rigtige svar var", self.random_number + self.random_number2)


range_start = 1
range_end = 20
game = Plus(range_start, range_end)
game.plus_learner()

# -
class Minus:
    def __init__(self, range_start, range_end):
        self.range_start = range_start
        self.range_end = range_end
        self.random_number = random.randint(range_start, range_end)
        self.random_number2 = random.randint(range_start, range_end)

    def minus_learner(self):
        print("minus stykke", self.random_number, "-", self.random_number2)
        svar = int(input())
        if svar == self.random_number - self.random_number2:
            print("Det er rigtigt, Godt gået")
        if svar != self.random_number - self.random_number2:
            print("Prøv igen")
        svar = int(input())
        if svar == self.random_number - self.random_number2:
            print("Det er rigtigt, godt gået")
        else:
            print("svaret er forkert, det rigtige svar var", self.random_number - self.random_number2)

range_start = 1
range_end = 20
game = Minus(range_start, range_end)
game.minus_learner()

# *
class Gange:
    def __init__(self, range_start, range_end):
        self.range_start = range_start
        self.range_end = range_end
        self.random_number = random.randint(range_start, range_end)
        self.random_number2 = random.randint(range_start, range_end)

    def gange_learner(self):
        print("gange stykke", self.random_number, "*", self.random_number2)
        svar = int(input())
        if svar == self.random_number * self.random_number2:
            print("Det er rigtigt, Godt gået")
        if svar != self.random_number * self.random_number2:
            print("Prøv igen")
        svar = int(input())
        if svar == self.random_number * self.random_number2:
            print("Det er rigtigt, godt gået")
        else:
            print("svaret er forkert, det rigtige svar var", self.random_number * self.random_number2)

range_start = 1
range_end = 20
game = Gange(range_start, range_end)
game.gange_learner()

print("slut")

# Keep the console open until Enter is pressed
input("Press Enter to exit...")
