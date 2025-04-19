#Gussing number game
secret_number=9
guess_count=0
while guess_count<3:
    Guess=int(input("Guess:"))
    guess_count+=1
    if Guess==secret_number:
        print("You Won!")
        break
else:
    print("Only 3 chance YOU LOSE")


