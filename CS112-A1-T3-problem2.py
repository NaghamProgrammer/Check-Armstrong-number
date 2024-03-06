# File: CS112-A1-T3-problem2.py
# Purpose: a program that checks if a positive integer is an Armstrong number or not
# Author: Nagham Wael Mohamed Elsayed
# ID: 20231189


# display a message and take input from user
num = input("please enter a positive integer: ")
# initialize sum
summ = 0
while True :
    try :
        # handle negative input and zero then ask user to input again
        while int(num) <= 0 :
            print('ERROR! please enter a positive integer only')
            num = input("please enter a positive integer: ")
        # loop through each individual digit in the number
        for i in num :
                # (sum) = (sum) + (each individual digit) ** (the total number of digits in the number)
                summ += int(i)**len(num)
        # the number is Armstrong if the sum of individual digits power total number of digits equals the number itself
        if summ == int(num) :
                print('the number is an Armstrong number')
        else:
                print('the number is not an Armstrong number')
        # break the loop and display the output if the input is valid
        break
    except ValueError :
        print('ERROR! please enter a positive integer only')
        num = input("please enter a positive integer: ")
        # the loop doesn't break until the input is valid


#test 1 ---> 0 (passed)
#test 2 ---> -4 (passed)
#test 3 ---> p (passed)
#test 4 ---> 4,8 (passed)
#test 5 ---> 153 (passed)
#test 6 ---> 9474 (passed)
#test 6 ---> 545 (passed)
#test 7 ---> 0 ---> 9 (passed)
#test 8 ---> p ---> 9 (passed)
#test 9 ---> 0 ---> p ---> 9 (passed)
#test 10 ---> p ---> 0 ---> 9 (passed)