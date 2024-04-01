# Customer Banking System
This application program is allows users to calculate and track interest earned on savings 
and CD accounts. By running this application, users will be able to enter their 
savings and CD account information, see the interest earned, and view the 
updated balances after a specified number of months.

## Technical details:
This application has following programs - 
```python
Accounts.py
```
### This program contains **Account** class definition. 
**Account** has following three methods:
- **init** This initializes the class by setting initial values for *balance* and *interest*
- **set_balance** This method updates **Account** instance *balance* based on input parameter value
- **set_interest** This method updates **Account** instance *interest* based on input parameter value  

```python
savings_account.py
```
### This program has a function **create_savings_account**
It receives three parameters *balance, interest_rate, months*.
It is used to create a savings account instance, calculates interest earned, and updates the account balance.
It returns *new balance and interest amount*

```python
cd_account.py
```
### This program has a function **create_cd_account**
It receives three parameters *balance, interest_rate, months*.
It is used to create a CD account instance, calculates interest earned, and updates the account balance.
It returns *new balance and interest amount*

```python
customer_banking.py
```
### When user executes this program, it will prompt the user to input Savings and CD Account's initial
balance amount, interest and maturity period values. 
Then it will call function **create_savings_account** and **create_cd_account** which will return 
interest and updated balance. Those values are displayed to the user. 

