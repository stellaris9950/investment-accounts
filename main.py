# investment

import random


def main():

    accounts = []
    # create list of random accounts
    for i in range(20):
        accounts.append(random.randrange(0, 5000))
    print(accounts)


    # loop
    loop = True
    while loop:
        print(f"MAIN MENU"
              "\n1. Print Accounts "
              "\n2. Deposits "
              "\n3. Withdrawal "
              "\n4. Count under $2000 "
              "\n5. Generous Donor "
              "\n6. Hacker Attack "
              "\n7. Exit")
        menu_choice = int(input("Enter option # "))

        # Print Accounts
        if menu_choice == 1:
            print("Account Balances:")
            for item in accounts:
                print(f"Account {accounts.index(item)}: {item}")

        # Deposits
        elif menu_choice == 2:
            account_selected = int(input("Enter account #:"))
            account_money_add = int(input("Enter amount to deposit:"))
            print(f"Account {account_selected} Previous balance: ${accounts[account_selected]}")
            accounts[account_selected] += account_money_add
            print(f"Account {account_selected} New Balance: ${accounts[account_selected]}")

        # Withdrawal
        elif menu_choice == 3:
            account_selected = int(input("Enter account #:"))
            account_money_removed = int(input("Enter amount to withdraw:"))
            if account_money_removed <= accounts[account_selected]:
                print(f"Account {account_selected} Previous balance: ${accounts[account_selected]}")
                accounts[account_selected] -= account_money_add
                print(f"Account {account_selected} New Balance: ${accounts[account_selected]}")
            else:
                print(f"Sorry, Insufficent funds.")

        # Count under $2000
        elif menu_choice == 4:
            under_2000_count = 0
            for item in accounts:
                if item < 2000:
                    print(f"Account {accounts.index(item)}: ${item}")
                    under_2000_count += 1
            print(f"Accounts with less that $2000: {under_2000_count}")

        # Generous Donor
        elif menu_choice == 5:
            under_2000_count = 0
            for item in accounts:
                if item < 2000:
                    account_index_store = accounts.index(item)
                    print(f"Account {account_index_store} Previous Balance: ${item}")
                    accounts[account_index_store] += 500
                    print(f"Account {account_index_store} New Balance: ${accounts[account_index_store]}")
                    under_2000_count += 1
            print(f"Total Money Donated: ${under_2000_count * 500}")

        # Hacker Attack
        elif menu_choice == 6:
            money_stolen_count = 0
            for item in accounts:
                money_stolen = item * 0.05
                accounts[accounts.index(item)] -= money_stolen
                money_stolen_count += money_stolen
            print(f"Total Stolen is: ${money_stolen_count}")

        # Exit
        elif menu_choice == 7:
            loop = False


# Call Function
main()
