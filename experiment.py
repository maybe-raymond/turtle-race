from race import *
import random
import turtle

#creating a random number for the distance
num=random.sample(range(100,600),6)

#making each turtle start at the same time , giving them speed and starting the race
turtle.delay(0.5)
steve.fd(num[0])
kray.fd(num[1])
lou.fd(num[2])
mike.fd(num[3])
matt.fd(num[4])
carl.fd(num[5])

#finding the highest number
high =max(num)

#determining the winner of the race
if high == num[0]:
    print("steve won")
elif high == num[1]:
    print("kray won")
elif high == num[2]:
    print("lou won")
elif high == num[3]:
    print("mike won")
elif  high == num[4]:
    print("matt won")
else :
    print("carl won")


turtle.done()
