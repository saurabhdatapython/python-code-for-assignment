class Atm:
    def __init__(self):
    
     self.pin=""
     self.balance=0
     self.menu()

    def menu(self):
     user_input=input("""
                       how would you like to proceed
                       1 enter 1 to create oin
                       2 enter 2 to deposit
                       3 enter 3 to withdraw
                       4 enter 4 to check balance
                       5 enter 5 to exit""")
    if user_input=="1":
     print("create pin")
    elif user_input=="2":
     print("deposit ")
    elif user_input==3:
     print("withdraw")
    elif user_input==4:
     print("check balance")
    elif user_input==5:
     print("bye")


     
