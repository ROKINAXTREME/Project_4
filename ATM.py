
import sys
import time
import random as ran
Name=input('Hello, what is your Name? ')
print('Welcome to the ATM at the national bank of coders!!! (ps, your card number is 87568903, and pin 7895)')
class ATM(object):
    def cardNumber():
        num=input('card number? ')
        if num=='87568903':
            print('Hello, '+Name+'!!!')
        elif num=='20080416':
            print('Hello, Aarav!!!')
        else:
            print('Invalid')
            exit()

    def pin():
        pin=input('Pin Number')
        if pin == '9076' or pin == '7895':
            print(Name+'...')
            print('Validated!!!')
        else:
            print('invalid')
            exit()
    def withdraw():
        balance=6789
        howMuch=input('How much do you want to withdraw?')
        howMuchint=int(howMuch)
        if howMuchint < balance:
            balance=int(balance)-howMuchint
            print('your balance is now, '+str(balance)+', don\'t forget to pick up your money!!!')
            print('''________________
|                |
|                |
|   $$$          |
|                |
|________________|''')
        if howMuchint>balance:
            print('Not enough money')

    def deposit():
        balance=6789
        howMuch=input('How much do you want to deposit?')
        howMuchint=int(howMuch)
        balance = balance+int(howMuch)
        print('Your balance is '+str(balance))
    def enquiry():
        if Name=='Aarav' or 'aarav':
            balance=str(6789)
        elif Name=='Shubha' or 'shubha':
            balance=str(89678)
        print('your balance is '+balance)
    cardNumber()
    pin()
    what=str(input('what is your transaction? (withdraw is 1, deposit is 2, enquiry is 3)'))
    if what=='1':
        withdraw()
    elif what=='2':
        deposit()
    elif what=='3':
        enquiry()
    elif what != ('1' or '2' or '3'):
        print('there is no transaction for the number '+what)
time.sleep(5)
