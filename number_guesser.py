import random
#r=random.randrange(-1,11)#-1 to 10
#random.randrange(11)#-0 to 10
#random.randint(11)#0 to 11

top_of_range=input("type a number: ")
if top_of_range.isdigit():
        top_of_range=int(top_of_range)
        if top_of_range<=0:
                print("Please type a number greater than zero next time")
                quit()
else:
    print("Please type a number next time")
    quit()
random_number=random.randint(0,top_of_range)#-1 to 11
guesses=0
while True:
       guesses+=1
       user_guess=input("Make a guess: ")
       if user_guess.isdigit():
              user_guess=int(user_guess)
       else:
              print("Please type a number text time")
              continue#Automatically goes to the top of the loop
       if user_guess==random_number:
              print("You got it!")
              break
       
       elif user_guess>random_number:
                print("You were above the number")
       else:
                print("You were below the number")
print("You got it in ",guesses," guesses")
print("You got it in " + str(guesses) + " guesses")


              
       