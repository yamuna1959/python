class Customer:
    "Common base class for all Customers"
    def getData(self,name,accno,acctype,balance):
        self.name=name
        self.accno=accno
        self.acctype=acctype
        self.balance=balance
    def displayCustomer(self):
        print("Customer Name:",self.name)
        print("Account Number:",self.accno)
        print("Account Type:",self.acctype)
        print("Balance amount:",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdrawal(self,amount):
        if self.balance-amount<0: print("Insufficient Funds")
        else: self.balance=self.balance-amount
ch=0
while ch!=5:
    print("1.New Customer")
    print("2.Deposit")
    print("3.Withdrawal")
    print("4.Display")
    print("5.Exit")
    ch=int(input("Enter your choie:"))
    if ch==1:
        obj=Customer()
        n=input("Enter Name:")
        no=int(input("Enter Account Number:"))
        t=input("Enter Account Type(SB/C):")
        b=int(input("Enter the Amount:"))
        obj.getData(n,no,t,b)
    if ch==2:
        b=int(input("Enter the amount to be a deposited:"))
        obj.deposit(b)
    if ch==3:
        b=int(input("Enter the amount to be withdrawn:"))
        obj.withdrawal(b)
    if ch==4:
        obj.displayCustomer()
else:print("Program Terminated")
