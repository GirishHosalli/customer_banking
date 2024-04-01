# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("\n")
    while True:
        try:
            savings_balance = float(input(f"Please enter current Savings Account Balance{' ':<7}: $ "))
            break
        except ValueError:
            print("Input error. Please enter an integer or a decimal value.")
        
    while True:
        try:
            savings_interest = float(input(f"Please enter Savings Account Interest Rate (%){' ':<5}: "))
            break
        except ValueError:
            print("Input error. Please enter an integer or a decimal value.")

    while True:
        try:
            savings_maturity = int(input(f"Please enter Savings Account Maturity (months){' ':<5}: "))
            break
        except ValueError:
            print("Input error. Please enter an integer.")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    # For writing interestGet spaces to pad for Interest line
    if len(str(savings_maturity)) == 1:
        int_spaces = ' ' * 7
    else:
        int_spaces = ' ' * 6

    print('-' * 65)
    print(f"For {savings_maturity} months Savings Account earned interest{int_spaces}: ${interest_earned: ,.2f}")
    print(f"Savings Account updated balance{' ':<20}: ${updated_savings_balance: ,.2f}")
    print('-' * 65)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print("\n")
    while True:
        try:
            cd_balance = float(input(f"Please enter current CD Account Balance {' ':<11}: $ "))
            break
        except ValueError:
            print("Input error. Please enter an integer or a decimal value.")

    while True:
        try:
            cd_interest = float(input(f"Please enter CD Account Interest Rate (%){' ':<10}: "))
            break
        except ValueError:
            print("Input error. Please enter an integer or a decimal value.")

    while True:
        try:
            cd_maturity = int(input("Please enter CD Account Maturity (number of months): "))
            break
        except:
            print("Input error. Please enter an integer.")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    if len(str(cd_maturity)) == 1:
        int_spaces = ' ' * 11
    else:
        int_spaces = ' ' * 10
        
    bal_spaces = ' ' * 24

    print('-' * 65)
    print(f"For {cd_maturity} months CD Account earned interest {int_spaces}: ${interest_earned: ,.2f}")
    print(f"CD Account updated balance {bal_spaces}: ${updated_cd_balance: ,.2f}")
    print('-' * 65)
    print("\n")

if __name__ == "__main__":
    # Call the main function.
    main()

