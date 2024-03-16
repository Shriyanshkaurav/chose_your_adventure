name = input("What Is your Name : ")
print("Welcome ",name," To this Adventure!!")

answer = input("You are on a dirt road,It has come to an end and you can go lef or right.which way yo want to chose? ").lower()

if answer == "left":
    answer = ("You Come to a river,You can Walk Around It or You can Swim across it.Type Walk if you want to walk OR type Swim if You Want to swim: ").lower()
    
elif answer =="right":
    pass

else:
    print("Not a Valid Option.You Lose!!")        