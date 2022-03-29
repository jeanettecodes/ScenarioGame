name = input("Enter your name: ")
print("Welcome", name, "to this scenario game!")

answer = input("You are on a dead end road. You can turn left or right. Which way would you like to turn? ").lower()

if answer == "left":
    answer = input("You come across a lion, you can walk around it or turnaround back to the dead end road? Type walk or turnaround. ").lower()
    
    if answer == "walk":
        print("You walked around the lion and was eaten by a dinosaur.")
    elif answer == "turnaround":
        print("You turned around and walked towards the dead end road and was chased and eaten by the lion's cub.")
    else:
        print("Option is not valid. You lose!")
    
elif answer == "right":
    answer = input("You see a quad bike. You can go on the quad bike for the rest of the journey or you can walk the distance? Type quad bike or walk. ").lower()
    
    if answer == "quad bike":
        print("You got the quad bike and the brakes were not working. You drove off a cliff and was attacked by eagles.")
    elif answer == "walk":
        answer = input("You walked along the road and saw a treasure pot in a tree. Do you want to climb the tree for the treasure pot, yes or no? ").lower() 
    
    if answer == "yes":
        print("You climbed the tree and got the treasure. You opened the treasure and found diamonds and gold. You WIN!")
    elif answer == "no":
        print("As you was about to walk off, the treasure pot fell on your head and you passed out. You LOSE!")
    else:
        print("Option is not valid. You lose!")

else:
    print("Option is not valid. You lose!")

print("Thank you for playing the game", name, "!")



