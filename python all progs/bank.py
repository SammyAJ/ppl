from random import randint,randrange
class BankAccount() :
	def __init__(self):
		print "Welcome to a bank system"
		self.__accno = input("Enter your account number")
		print "Your acoount number is"
		print self.__accno
		self.accname = "Ajinkya Geetanand Chavan"
		print "Hello"
		print self.accname
		self.lad = "1.12.16"
		print "last date of access is :"
		print self.lad
		self.bal = 10000
		print "You have balance "
		print self.bal
		

class Transaction() :
	def __init__(self):
		print "Transaction process Started"
		self.tid = randint(100000,10000000)
		print "The traction id is"
		print self.tid
		self.ttype = raw_input("Enter your account Type")
		print "Your account type is"
		print self.ttype
		self.bal = 10000
		self.accname = "Ajinkya Geetanand Chavan"
	def credit(self) :
		self.amt = input("Enter amount to credit")
		self.bal = self.bal + self.amt
		print "Your amount is succesfully credited"
	def PrintStatus(self) :
		#print "Your Account Number is :"
		#print self.accno
		print "Your Transaction ID is :"
		print self.tid
		print "Your Trsaction type is :"
		print self.ttype
		print "Your Trasaction Amount is :"
		print self.amt
		print "Your current balance is :"
		print self.bal
		print "Thank you :)"
		print self.accname
	def debit(self) :
		self.amt = input("Enter amount to credit")
		self.bal = self.bal - self.amt
		print "The amount is succesfully debited"
		


c = BankAccount()
d = Transaction()
print "1)CREDIT"
print "2)DEBIT"
p = input("Enter your choice");
if (p == 1) :
	d.credit()
	d.PrintStatus()
elif(p == 2) :
	d.debit()
	d.PrintStatus()
else :
	print "You eneter worng choice"








