#This is a ATM program
#intsert the card
#enter 4 digit PIN
#validate PIN
#if PIN validated then, ask what do you want to do with this card
#balance enquiry
#you have (money amount) in your acount
#deposit
#enter amout to deposit
#withdraw
#enter amount to withdraw
#don't forget to collect ur cash!!
print('Welcome to the ATM at the national bank of coders!!! (ps, your card number is 87568903, and pin 7895)')
class ATM(object):
    def __init__(self, cardNumber, pin, withdraw, deposit, enquiry):
        self.cardNumber=cardNumber
        self.pin=pin
        self.withdraw=withdraw
        self.deposit=deposit
        self.enquiry=enquiry
    def cardNumber(self):
        print('Hello!')
    def pin(self):
        print('Validated!')
    def withdraw(self):
        print('Withdrawn')
    def deposit(self):
        print('Deposited')
    def enquiry(self):
        print('your balance is '+random.randint(43523, 6784545))
Aarav=ATM(20080416, 7654, 0, 1, 6)
Shubha=ATM(87568903, 7895, 0, 9, 13)
name=input('What is your name?')
if name=='Aarav':
    print(Aarav)
if name=='Shubha':
    print(Shubha)
