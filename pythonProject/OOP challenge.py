class Account:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def depoist_fund(self,amount_added):
        self.balance += amount_added

    def withdraw_fund(self,withdrawn_amount):
        if withdrawn_amount > self.balance:
            print("Cant Withdraw fund: Insufficient Funds")
        else:
            self.balance -= withdrawn_amount

    def show_balance(self):
        return self.balance

    def __str__(self):
        return "Name: " + self.name+"\n"+"Balance: " + str(self.balance) + " AED"

class VIP(Account):

    def __init__(self, vip_account,name,balance=0):
        self.vip_account = vip_account
        self.balance = balance
        self.name = name

    def if_vip_account(self,vip_account):
        if vip_account == True:
            return True
        else:
            return False

    def vip_account_bonus(self):
        self.balance += 10000

    def __str__(self):
        return f"VIP Customer Name: {self.name}\n Balance: {self.balance} "


account1 = Account("Abdel Magid",34531.34)
vip_account1 = VIP("Abdel Magi",True)

is_vip_account = vip_account1.if_vip_account(True)

if is_vip_account:
    print('Congratulation you are a VIP Customer, you get a 10000 bonus to your account balance')
    vip_account1.vip_account_bonus()

print(vip_account1.show_balance())
vip_account1.withdraw_fund(5000)
print(vip_account1.show_balance())