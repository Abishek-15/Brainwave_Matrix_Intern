from cardholder import cardholder

def print_menu():
    ###print options to the user
    print("Please choose from one of the following options...")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Show Balance")
    print("4.Exit")


def deposit(cardholder):
    try:
        deposit = float(input("How much money would you like to deposit: "))
        cardholder.set_balance(cardholder.get_balance() + deposit)
        print("Thank you for your money. your new balance is: ", str(cardholder.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardholder):
    try:
        withdraw = float(input("How much money would you like to withdraw: "))
        ##check if user has enough money
        if(cardholder.get_balance() < withdraw):
            print("Insufficient balance :(")
        else:
            cardholder.set_balance(cardholder.getbalance() - withdraw)
            print("Thank you for using our ATM")
    except:
         print("Invalid Input")

def check_balance(cardholder):
    print("your current balance is: ", cardholder.get_balance())


if __name__ == "__main__":
    current_user = cardholder("","","","","")

    ##create a repo of cardholders
    list_of_cardholders = []
    list_of_cardholders.append(cardholder("467667565897", 1234, "john", "griffith", 150.31))
    list_of_cardholders.append(cardholder("328765219780", 5676, "ray", "parker", 310.25))
    list_of_cardholders.append(cardholder("735681290745", 1487, "jane", "white", 105.59))
    list_of_cardholders.append(cardholder("678312459007", 3754, "dwayne", "ackerman", 851.84))
    list_of_cardholders.append(cardholder("209655432178", 2879, "erwin", "smith", 54.27))


  ##prompt user for debit card number
    debitCardNum = ""
   
    while True:
       try:
           debitCardNum = input("Please insert your debit card: ")
           #check against repo
           debitMatch = [holder for holder in list_of_cardholders if holder.cardNum == debitCardNum]
           if(len(debitMatch) > 0):
               current_user = debitMatch[0]
               break
           else:
                print("Card number not recognized. please try again.")
       except:
            print("Card number not recognized. please try again.")

      ##prompt for pin
            while True:
                try:
                    userPin = int(input("Please enter your pin: ").strip())
                    if(current_user.get_pin() == userPin):
                        break
                    else:
                        print("Invalid PIN. Please try again.")
                except:
                    print("Invslid PIN. Please try again.")

         ##print options
                    print("Welcome ", current_user.get_firstname())
                    option = 0
                    while (option != 4):
                        print_menu()
                        try:
                            option = int(input())
                        except:
                            print("Invalid Input. Please try again.")


                        if(option == 1):
                            deposit(current_user)
                        elif(option == 2):
                            withdraw(current_user)
                        elif(option == 3):
                            check_balance(current_user)
                        elif(option == 4):
                            break
                        else:
                            option == 0

                    print("Thank you, Have a nice day ")            

