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
    while True:
        try:
            savings_balance = float(input("Please enter Savings Account Balance: $ "))
            break
        except ValueError:
            print("Input error. Please enter an integer or a decimal value.")
        
    while True:
        try:
            savings_interest = float(input("Please enter Savings Account Interest Rate: "))
            break
        except ValueError:
            print("Input error. Please enter an integer or a decimal value.")

    while True:
        try:
            savings_maturity = int(input("Please enter Savings Account Maturity (number of months): "))
            break
        except ValueError:
            print("Input error. Please enter an integer.")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"CD Account earned interest amount: {interest_earned: ,.2f}")
    print(f"CD Account updated balance amount: {updated_savings_balance: ,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    while True:
        try:
            cd_balance = float(input("Please enter CD Account Balance: $ "))
            break
        except ValueError:
            print("Input error. Please enter an integer or a decimal value.")

    while True:
        try:
            cd_interest = float(input("Please enter CD Account Interest Rate: "))
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
    print(f"CD Account earned interest amount: {interest_earned: ,.2f}")
    print(f"CD Account updated balance amount: {updated_cd_balance: ,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()