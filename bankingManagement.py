class User:
    def __init__(self) -> None:
        self.name = ''
        self.email = ''
        self.password = ''
        self.single_user_balance = 0
        self.transaction_history = []
        super().__init__()
        

    def create_account(self, name, email, password):
        self.name = name
        self.email = email 
        self.password = password
    
    def deposit_amount(self, amount):
        if amount >0:
            self.single_user_balance += amount
            self.transaction_history.append(f"Deposit {amount}")
        else:
            print("Amount couldn't be negative.")
    
    def  withdrawal_amount(self, amount):
        if amount > 0:
            if amount < self.single_user_balance:
                self.single_user_balance -= amount
                self.transaction_history.append(f"withdrawal {amount}")
                print(f"Hey {self.name} Your withdrawal_amount is here: {amount} \n After Withdraw, You has this balance in your account. {self.check_available_balance()}")
            else:
                print(f"Hey {self.name}: You have insufficient balance in your account.")
        else:
            print("Amount couldn't be negative.")
    
    def check_available_balance(self):
        return self.single_user_balance

    def transfer_amount(self, other_user, transfer_balance):
        if transfer_balance > 0:
            if transfer_balance < self.single_user_balance:
                self.single_user_balance -= transfer_balance
                self.transaction_history.append(f" {transfer_balance} tk transfer to {other_user.name}")
                other_user.deposit_amount(transfer_balance)
            else:
                print("You have insufficient balance in your account.") 
        else:
            return "Amount couldn't be negative."

    def check_transaction_history(self):
        return self.transaction_history
    
    def take_loan(self, amount):
        if amount != None:
            self.transaction_history.append(f"Loan: {amount}")
            self.single_user_balance += amount
        

# admin class
class Admin(User):
    def __init__(self) -> None:
        self.__bank_balance = 0
        self.__total_bank_loan = 0
        self.__loan_feature = False
        super().__init__()
        

    def create_account(self, name, email, password):
        return super().create_account(name, email, password)

    def add_bank_balance(self, *total_balance_Of_all_user):
        for user in total_balance_Of_all_user:
            self.__bank_balance += user.check_available_balance()

    def check_available_bank_balance(self):
        return self.__bank_balance
    
    def is_loan_feature_active(self):
        if self.__loan_feature == True:
            return True
        else:
            return False
        
    def  given_loan(self, user_balance):
        if self.is_loan_feature_active() == True:
            if user_balance < self.__bank_balance:
                if user_balance * 2 < self.__bank_balance:
                    self.__total_bank_loan += user_balance * 2
                    self.__bank_balance -= user_balance * 2
                    return user_balance * 2
                else:
                    print("Bank has no sufficent balance. ")
            else:
                print( "Bank is crupt.")
        else:
            print("Loan Feature is disabled")
    
    def loan_featureEnable(self):
        self.__loan_feature = True
    
    def loan_featureDisabled(self):
        self.__loan_feature = False

    def check_total_loan_amount(self):
        return self.__total_bank_loan



user1 = User()
user2 = User()
user3 = User()

admin = Admin()

# For User 1
user1.create_account("rahim", "rahim@gmial.com", 12345)

user1.deposit_amount(5000)
print("User1 Account Balance: ", user1.check_available_balance())

user1.withdrawal_amount(200)
print("User1 Account Balance: ", user1.check_available_balance())

user1.transfer_amount(user2, 50)
print(user1.check_transaction_history())
print("User1 Account Balance: ", user1.check_available_balance())
user1.take_loan(admin.given_loan(user1.check_available_balance()))

# check bank total balance
admin.add_bank_balance(user1)
print("Total Bank Balance: ",admin.check_available_bank_balance())

# enable loanFeature
admin.loan_featureEnable()
print("\t\t---------After LoanFeature enable---------")
user1.take_loan(admin.given_loan(user1.check_available_balance()))
print("Total Bank Balance: ",admin.check_available_bank_balance())


# User2 information
user2.create_account("Muhib", "muhgib@gmial.com", 19845)
print("User2 Account Balance: ", user2.check_available_balance())

print("\t\t----------User2 information-----")
user2.deposit_amount(400)
print("User2 Account Balance: ", user2.check_available_balance())

user2.withdrawal_amount(100)
print("User2 Account Balance: ", user2.check_available_balance())

user2.transfer_amount(user1, 50)
admin.add_bank_balance(user2)


print("User2 Account Balance: ", user2.check_available_balance())
user2.take_loan(admin.given_loan(user2.check_available_balance()))
print(user2.check_transaction_history())

# check bank total balance

print("User2 Account Balance: ", user2.check_available_balance())
print("Total Bank Balance: ",admin.check_available_bank_balance())
