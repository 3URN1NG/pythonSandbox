# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:19:59 2019

@author: Simon
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rndm

def rolereddice():
        r = rndm.randint(1,6)
        if r==1:
                return 9
        else:
                return 4
        
def rolebluedice():
        r = rndm.randint(1,6)
        if r<4:
                return 7
        else:
                return 2
        
def roleolivedice():
        r = rndm.randint(1,6)
        if r<6:
                return 5
        else:
                return 0
        
def roleyellowdice():
        r = rndm.randint(1,6)
        if r<3:
                return 8
        else:
                return 3
        
def rolemagentadice():
        r = rndm.randint(1,6)
        if r<5:
                return 6
        else:
                return 1

def calculateRoundsWithDices(rounds, dice, red, blue, olive, yellow, magenta):
        winsred = 0
        winsblue = 0
        winsolive = 0
        winsyellow = 0
        winsmagenta = 0
        winstwowinners = 0
        
        for i in range(rounds):
                #print("Round ", i)
                participants = []
                if red == 1:
                        r = 0
                        for j in range(dice):
                                r += rolereddice()
                        participants += [r]
                if blue == 1:
                        b = 0
                        for j in range(dice):
                                b += rolebluedice()
                        participants += [b]
                if olive == 1:
                        o = 0
                        for j in range(dice):
                                o += roleolivedice()
                        participants += [o]
                if yellow == 1:
                        y = 0
                        for j in range(dice):
                                y +=  roleyellowdice()
                        participants += [y]
                if magenta == 1:
                        m = 0
                        for j in range(dice):
                                m += rolemagentadice()
                        participants += [m]
                
                winingNumber = max(participants)
                #print("Highest number this round: ", winingNumber)
                winner = "Evaluation failed"
                numberofwinners = 0
                if (red == 1 and r == winingNumber):
                        winsred += 1
                        winner = "Red"
                        numberofwinners += 1
                if (blue == 1 and b == winingNumber):
                        winsblue += 1
                        winner = "Blue"
                        numberofwinners += 1
                if (olive == 1 and o == winingNumber):
                        winsolive += 1
                        winner = "Olive"
                        numberofwinners += 1
                if (yellow == 1 and y == winingNumber):
                        winsyellow += 1
                        winner = "Yellow"
                        numberofwinners += 1
                if (magenta == 1 and m == winingNumber):
                        winsmagenta += 1
                        winner = "Magenta"
                        numberofwinners += 1
                if (numberofwinners > 1):
                        winstwowinners += 1
                        if (red == 1 and r == winingNumber):
                                winsred -= 1
                                winner = "Red"
                        if (blue == 1 and b == winingNumber):
                                winsblue -= 1
                                winner = "Blue"
                        if (olive == 1 and o == winingNumber):
                                winsolive -= 1
                                winner = "Olive"
                        if (yellow == 1 and y == winingNumber):
                                winsyellow -= 1
                                winner = "Yellow"
                        if (magenta == 1 and m == winingNumber):
                                winsmagenta -= 1
                                winner = "Magenta"
                #print("Winner in round ", i, ": ", winner)
                #print()
        print()
        results = []
        results += [winstwowinners]
        print("Games with atleast two winners:", winstwowinners)
        if (red == 1):
                print("Games won by red: ", winsred)
                results += [winsred]
                
        if (blue == 1):
                print("Games won by blue: ", winsblue)
                results += [winsblue]
                
        if (olive == 1):
                print("Games won by olive: ", winsolive)
                results += [winsolive]
                
        if (yellow == 1):
                print("Games won by yellow: ", winsyellow)
                results += [winsyellow]
                
        if (magenta == 1):
                print("Games won by magenta: ", winsmagenta)
                results += [winsmagenta]
                
        return results

dice = int(input("Input number of dice:"))
print("Number of dice choosen: ", dice)

rounds = int(input("Input number of rounds:"))
print("Number of rounds choosen: ", rounds)

red = int(input("Red?"))
print("Red included:", red)

blue = int(input("Blue?"))
print("Blue included:", blue)

olive = int(input("Olive?"))
print("Olive included:", olive)

yellow = int(input("Yellow?"))
print("Yellow included:", yellow)

magenta = int(input("Magenta?"))
print("Magenta included:", magenta)

colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

print()
print()
for i in range(dice+1):
        if (i>0):     
                print("Number of dice per color:", i)
                result = calculateRoundsWithDices(rounds, i, red, blue, olive, yellow, magenta)
                participants = []
                participants += ["evens"]
                if (red == 1):
                        participants += ["red"]
                if (blue == 1):
                        participants += ["blue"]
                if (olive == 1):
                        participants += ["olive"]
                if (yellow == 1):
                        participants += ["yellow"]
                if (magenta == 1):
                        participants += ["magenta"]
                plt.plot(participants, result, color=colors[i%7], marker = 'o', linestyle = '--')
                print("Color of", i, "dice:", colors[i%7])
                print()
                print()
plt.grid(True)
plt.ylabel('number of wins')
plt.xlabel('color')
plt.show()