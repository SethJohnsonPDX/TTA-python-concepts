# Python:   2.7.13
# Date:     10-4-2017
# Author:   Seth R. Johnson
#
# Purpose:  The Tech Academy - Python Course, Item 36 Drill
#           
#! /usr/bin/env python
# -*- coding: utf-8 -*-


def start(your_name="",amount=0):
    your_name = raw_input("\nWhat's your name? ").capitalize()
    print("\nHey there, {}! I'm going to ask you a few questions.".format(your_name))
    amount = friends(amount)

def friends(amount):
    amount = int(raw_input("\nHow many friends do you have?: "))
    if amount > 5:
        print("\n{} friends!? You're popular.".format(float(amount)))
    else:
        stop = True
        while stop:
            if amount < 5:
                amount = int(raw_input("\nI don't believe you, how many friends do you really have?"))
                if amount == 5:
                    print("\n{} friends!? Same here!".format(float(amount)))
                    stop = False
    amount = nameFriends(amount)

    
def nameFriends(amount):
    best = raw_input("List your best friend.").capitalize()
    print("{} is best, got it.".format(best))
    second = raw_input("List your second best friend.").capitalize()
    print("{} is second best, got it.".format(second))
    third = raw_input("List your third best friend.").capitalize()
    print("{} is third best, got it.".format(third))
    names = [best,second,third]
    for rank in names:
        print("One friend is:",rank)
        
    amount = mathFun(amount)

def mathFun(amount):
    addition = amount + 1
    print(addition)
    subtraction = amount - 1
    print(subtraction)
    multiplication = amount * 3
    print(multiplication)
    division = multiplication / 5
    print(division)
    x = division
    y = multiplication
    y += x
    print(y)
    modulus = amount % division
    print(modulus)
    
    if (amount and y) > 5:
        print("{} and {} are greater than {}".format(amount,y,5))
    elif (amount or y) > 5:
        print("One of these are greater than {}".format(5))
    else:
        print("None of these are greater than ".format(5))

    tupleFun = (multiplication, x, modulus, amount)

    for position in tupleFun:
        print( "Tuple value is", position)
    




if __name__ == "__main__":
    start()
