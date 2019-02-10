import time
import sys

def write(string):
    for i in string:
        print(i, end = '')
        sys.stdout.flush()
        time.sleep(.04)

blah = "You have been selected by the CIA to solve these series of tasks... "
for l in blah:
    print(l, end = '')
    sys.stdout.flush()
    time.sleep(0.04)
print ()
zlah = "Codes have been used throughout history whenever people wanted to keep messages private."
for l in zlah:
    print(l, end = '')
    sys.stdout.flush()
    time.sleep(0.04)
print()
message = "It is your task to solve these encoded messages"
for l in message:
    print(l, end = '')
    sys.stdout.flush()
    time.sleep(0.04)
print()

def endGame():
    print("Congratulations! You win! Thanks for playing our game!")
    write("Until next time..." + '\n\n')
    print("Created by Benjamin Preiser, Joel Faynshmidt, Naman Garg, and Vikrant Bakshi")

def level9():
    write("Now that we have no more use for you, prepare to be terminated.")
    print()
    print("*As the walls close in on you, you notice the wall seems weaker in one area*")
    while input != "YES" or input != "NO":
        choice = input("Do you choose to try to break it? (YES/NO) ")
        if(choice == "YES"):
            print("The wall caves in, and you escape.")
            break
        elif(choice == "NO"):
            print("You are terminated.")
            break
    if(choice == "YES"):
          endGame()

def Level8():
    write("THINGS ARE GETTING WILD")
    print()
    level9()

def Level7():##
    write("Level 7")
    print()
    write("YOU ARE A WORLD HERO." + '\n'+"YOU ARE FREE FROM THE CIA.")
    print()
    write("STILL THERE?")
    print()
    input("YES/NO?")
    print()
    Level8()

def Level6():##QWERTY KEYBOARD
    print("AREA 51")
    print("ALIENS!")
    print("COMMUNICATE? ")
    i=input("YES/NO ")
    if i=="YES":
        print("GOOD CHOICE")
        print("THEY SAY: UKTTZOFUL IXDQFGOR")
        j=input("ENTER YOUR RESPONSE IN ALL CAPITALS    ")
        if j=="GREETINGS HUMANOID":
            print("THEY SEEM FRIENDLY, GOOD JOB")
            Level7()
        else:
            print("THINK QWERT KEYBOARDS")
            while j!="GREETINGS HUMANOID":
                Level6()
    else:
        print("TRY AGAIN!")
        k=input("YES/NO")
        if k=="YES":
            print("GOOD CHOICE")
            print("THEY SAY: UKTTZOFUL IXDQFGOR")
            l=input("ENTER YOUR RESPONSE IN ALL CAPITALS    ")
            if l=="GREETINGS HUMANOID":
                print("THEY SEEM FRIENDLY, GOOD JOB")
                Level7()
            else:
                print("THINK QWERT KEYBOARDS")
                while j!="GREETINGS HUMANOID":
                    Level6()
        else:
            print("TRY AGAIN")
            m=input("YES/NO")
            while m=="NO":
                print("TRY AGAIN")
                m=input("YES/NO")
                if m=="YES":
                    print("GOOD CHOICE")
                    print("THEY SAY: UKTTZOFUL IXDQFGOR")
                    z=input("ENTER YOUR RESPONSE IN ALL CAPITALS    ")
                    if z=="GREETINGS HUMANOID":
                        print("THEY SEEM FRIENDLY, GOOD JOB")
                        Level7()
                    else:
                        print("THINK QWERTY KEYBOARDS")
                        while z!="GREETINGS HUMANOID":
                            Level6()

def Level4():#messageletter fake letter message letter fake letter
    print("LEVEL 4")
    print("HAERLUP UASY")
    i=input("ENTER YOUR RESPONSE IN ALL CAPITALS    ")
    if i=="HELP US":
        print("FANTASTIC")
        Level6()
    else:
        print("NOT ALL LETTERS HAVE MEANINGS")
        while i!="HELP US":
            Level4()

def Level3():##add one letter
    print("LEVEL 3")
    print("UIF FOE JT OFBS")
    i=input("ENTER YOUR RESPONSE IN ALL CAPITALS    ")
    if i=="THE END IS NEAR":
        print("IMPRESSIVE WORK")
        Level4()
    else:
        print("MAYBE ADD ONE")
        while i!="THE END IS NEAR":
            Level3()

def Level2(): ##A=Z,B=Y,C=X
    write("LEVEL 2")
    print()
    write("BLFI ORUV RH RM WZMTVI")
    print()
    i=input("ENTER YOUR RESPONSE IN ALL CAPITALS    ")
    if i=="YOUR LIFE IS IN DANGER":
        write("GREAT WORK CHIEF!")
        Level3()
    else:
        print("TRY THINKING IN REVERSE...")
        while i!="YOUR LIFE IS IN DANGER":
            Level2()

def Level1():
    m1 = " 23 5   1 18 5   23 1 20 3 8 9 14 7"
    prompt = "Decode the following message"
    print(prompt)
    print()

    for l in m1:
        print(l, end = '')
        sys.stdout.flush()
        time.sleep(0.05)

    var = input("Enter your response IN ALL CAPITAL LETTERS: \n")
    if(var == "WE ARE WATCHING"):
        print("Great work.")
        Level2()

    else:
        print("Response was incorrect try again. \n")
        while var != "WE ARE WATCHING":
            Level1()

def trainingMission():
    #backwards message
    write("Welcome. Before we assign you more difficult tasks we would like to make sure you can crack a simple code. Let's begin." + '\n' + "TNEMNGISSA TSRIF RUOY DETELPMOC EVAH UOY SNOITALUTARGNOC" + '\n' + "Please enter your answer in only capital letters: ")
    solved = False
    ans = input()
    tries = 0
    while solved == False:
        if(ans == "CONGRATULATIONS YOU HAVE COMPLETED YOUR FIRST ASSIGNMENT"):
            solved = True
        else:
            if tries == 3:
                write("Hint: The answer may present itself if you look from a different perspective.")
                print()
            write("Incorrect. Please try again: ")
            ans = input()
            tries = tries + 1
    Level1()

trainingMission()
