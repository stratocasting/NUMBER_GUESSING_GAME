import random
answer = random.randint(0,101)
def loop():
    guess = int(input("make a guess between 0-100"))
    if guess < answer:
        print ("too low")
    elif guess > answer:
        print ("too high")
    else:
        print (f"correct answer is {answer}, you win")
difficulty = input("easy or hard?")
if difficulty == "easy":
    health = 10
else:
    difficulty = 5
for x in range(health):
    remainder = health
    loop()
    health -= 1
    print (f"{health} turn remaining")



