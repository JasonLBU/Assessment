def CreatePassword():
    import random
    WORDS = ["red","blue","green","yellow","orange","monkey","zebra","lion","gorilla","giraffe","tower","closet","coal",
             "mouse","tiger","computer","monitor","water","earth","angry","lively","willing","cranky","calm","turtle",]
    while True:
        try:
            PasswordNum = int(input("Please enter how many passwords you'll need: "))
            if (0 < PasswordNum < 25):
                break
            else:
                print("Invalid number range. Please try again")
        except:
            print("Invalid input. Please try again.")
    for i in range(1,PasswordNum+1):
        RandPass = "".join(random.choices(WORDS,k=3))
        print(str(i) + "-->" + str(RandPass))
print("Password Generator\n==================")
CreatePassword()