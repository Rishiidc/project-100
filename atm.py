class atm:
    def __init__(self,type,balanceenquiry,cardnumber,cashwithdrawl):
        self.type = type
        self.balanceenquiry = balanceenquiry
        self.cardnumber = cardnumber
        self.cashwithdrawl = cashwithdrawl
    def enquiry(self):
        print("Balance Enquiry ->"+str(self.balanceenquiry))
        print("Your card number ->"+str(self.cardnumber))
        print("Quantity ->"+str(self.cashwithdrawl))
        print("Cash Type ->"+self.type)
    def buy(self):
        if(self.cashwithdrawl>0):
            self.cashwithdrawl -= 1 
            print("You have some balance in your account")
        else:
            print("You have no balance in your account")
    def sell(self):
        self.cashwithdrawl += 1
        print("Thank you for using this ATM")

#Using own details
coins = atm("coins",10000,236942392349,500)
cashnotes = atm("cashnotes",50000,236942392349,10000)

coins.buy()
cashnotes.enquiry()