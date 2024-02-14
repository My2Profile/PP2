def guess_random_number(random_number,number,name):
    cnt=0
    if(random_number==int(number)):
        print("Good job, "+name+"!","You guessed my number in",cnt, " guesses!")
        return
    while True:
     if(random_number==int(number)):
        print("Good job, "+name+"!","You guessed my number in", cnt, " guesses!")
        return
     else:
        print("Your guess is too low.")
        print("Take a guess")
        cnt+=1
        number=int(input())
        print()


 

import random
random_number=random.randint(0,20)
print("Hello! What is your name?")
name=input()
print()
print("Well, "+name, "I am thinking of a number between 1 and 20.")
print("Take a guess")
number=input()
print()
guess_random_number(random_number,number,name)