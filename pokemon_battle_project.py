#Your going to create a pokemon battle text story
#I've started it for you and given you some basis, but feel free to go whatever direction you'd like with this
#Here are some resources to learn more about python:
#https://www.codecademy.com/learn/learn-python
#py4e.com/lessons
#https://www.youtube.com/watch?v=WGJJIrtnfpk



print("Welcome to Pokemon Showdown!!!\n")

print("Dr Oak has 3 pokeballs for you to choose from, please choose a pokemon to be your partner!\n")
print("You have the choice of Bulbasuar, Charmander, or Squirtle")


choice = input("Filler text").upper() #Replace "Filler text" with the starter pokemon selection
while choice != "x" and choice != "x" and choice != "x": #replace the "x" with the letter that will identify each pokemon (make them upper case letters)
    print("Not a valid choice please try again!\n")
    choice = input("Filler text").upper() #Replace "Filler text" with the starter pokemon selection

if choice == "x": 
    pokemon = "pokemon 1" 
elif choice == "x":
    pokemon = "pokemon 2"
else: 
    pokemon = "pokemon 3"

print("\nYou choose " + pokemon + "!!!!!\n")


print("After leaving Dr Oak's lab, you decide to venture out to the wilderness.")
print("Not long after you venture out, you are walking through some long grass when.......")


print("WILD POKEMON ENCOUNTER\n")

print("You have encountered a wild Pidgey!!!")
print("Let's go " + pokemon)

print("\nYou have two attacks; Thrash and Stomp")

#Now you will do the check for the correct input as was done above when choosing your pokemon
#hint: use a single letter input and compare the input with that letter like input != "X"


#Finish off the story however you like, your options are endless!



#If you'd like a challenge, you can make it that the pokemon you are battling has HP (health points)
#you can then have you attacks do different amount of damange (ex. Thrash does 15 damage, Stomp does 20 damage)
#now you can have an enemy HP variable, and subtract the amount of damage each attack does depending on what attack is done
#and the battle does not end till the opponent's HP is below 10!