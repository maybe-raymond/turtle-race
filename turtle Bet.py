import random
import turtle

for i in range(3):
    print("Are you ready to bet on your turtle")
    answer = input("yes or no :")
    if answer == "yes":
        print("type the number of the turtle you think is going to win")
        print("1 STEVE ")
        print("2 CARL")
        print("3 MIKE ")
        print("4 LOU")
        print("5 MATT")
        print("6 KRAY")
        player1 = input("place your bet player 1: ")
        player2 = input("Place your bet player 2: ")
        player3 = input("place your bet player 3: ")

        #importing the race modual that will create the turtles
        from race import *
        #creating a random sample of numbers for the turtles distance
        num = random.sample(range(100, 600), 6)
        #making each turtle start at the same time , giving them speed and starting the race
        turtle.delay(0.5)
        steve.fd(num[0])
        carl.fd(num[1])
        mike.fd(num[2])
        lou.fd(num[3])
        matt.fd(num[4])
        kray.fd(num[5])

        #finding the highest number
        high =max(num)

        #determining the winner of the race for player 1
        if (high == num[0]) and (player1 == "1"):
            print("player 1 wins")
        elif (high == num[1]) and (player1 == '2') :
            print("player 1 wins")
        elif (high == num[2]) and (player1 == "3"):
            print("player 1 wins ")
        elif (high == num[3]) and (player1 == "4"):
            print("player 1 wins ")
        elif (high == num[4]) and (player1 == "5"):
            print("player 1 wins ")
        elif (high == num[5]) and (player1 == "6"):
            print("player 1 wins ")

        #determing the winner for player 2
        elif (high == num[0]) and (player2 == "1"):
            print("player 2 wins ")
        elif (high == num[1]) and (player2 == "2"):
            print("player 2 wins ")
        elif (high == num[2]) and (player2 == "3"):
            print("player  wins ")
        elif (high == num[3]) and (player2 == "4"):
            print("player 2 wins ")
        elif (high == num[4]) and (player2 == "5"):
            print("player 2 wins ")
        elif (high == num[5]) and (player2 == "6"):
            print("player 2 wins ")

        #Determing the winner for player 3
        elif (high == num[0]) and (player3 == "1"):
            print("player 3 wins ")
        elif (high == num[1]) and (player3 == "2"):
            print("player 3 wins ")
        elif (high == num[2]) and (player3 == "3"):
            print("player 3 wins ")
        elif (high == num[3]) and (player3 == "4"):
            print("player 3 wins ")
        elif (high == num[4]) and (player3 == "5"):
            print("player 3 wins ")
        elif (high == num[5]) and (player3 == "6"):
            print("player 3 wins ")
        # no one wins
        else:
            print("you all bet wrong, please try again ")


    else:
        print("come again next time ")
        break
