'''import random
for x in range(5,11):

    a = "Guess a Number"
    b = "Random bumber"
    a = int(input("Enter a random number between 5 to 10 : "))
    b = random.randint(5,10)
    if a == b:
        print("You won :) ")
    else:
        print("You lost :( ")
    print("The Random number was: ", b )'''



import random
for x in range(5,11):
    guessnum =int(input("Enter the guess number: "))
    randomnum = random.randint(5,10)
    if guessnum == randomnum:
         print("You won :)")
    else:
         print("You lost :(")
    print("The random number was: ", randomnum)