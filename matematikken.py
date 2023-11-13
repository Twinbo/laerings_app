import random

print("start")
print()
#random number 1
random_number = random.randint(1, 20)
print("første nummer =", random_number)

#random number 2
random_number2 = random.randint(1, 20)
print("anden nummer =", random_number2)


print()

#math thing

#+
class plus:
    print("plus stykke",random_number,"+",random_number2)
    svar = int(input())
    if svar == random_number+random_number2:
        print("Det er rigtigt, Godt gået")
    if svar != random_number+random_number2:
        print("Prøv igen")
    svar = int(input())
    if svar == random_number+random_number2:
        print("Det er rigtigt, godt gået")
    else:
        print("svaret er forkert, det rigtige svar var", random_number+random_number2)

#-
class minus:
    print("minus stykke",random_number,"-",random_number2)
    svar = int(input())
    if svar == random_number-random_number2:
        print("Det er rigtigt, Godt gået")
    if svar != random_number-random_number2:
        print("Prøv igen")
    svar = int(input())
    if svar == random_number-random_number2:
        print("Det er rigtigt, godt gået")
    else:
     print("svaret er forkert, det rigtige svar var", random_number-random_number2)

#*
class gange:
    print("gange stykke",random_number,"*",random_number2)
    svar = int(input())
    if svar == random_number*random_number2:
        print("Det er rigtigt, Godt gået")
    if svar != random_number*random_number2:
        print("Prøv igen")
    svar = int(input())
    if svar == random_number*random_number2:
     print("Det er rigtigt, godt gået")
    else:
     print("svaret er forkert, det rigtige svar var", random_number*random_number2)

print("slut")
#test


