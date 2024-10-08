# Expense-Tracker

The Expense Tracker is a Python application that allows users to manage and track their expenses using an Excel file (exp_page.xlsx). It utilizes the pandas library for data manipulation and provides various functionalities such as viewing the expense table, adding new entries, calculating sums within a date range, and exiting the system.

# Requirements
 - Python 3.x

 - pandas library (pip install pandas)

 - openpyxl library (automatically installed with pandas for Excel file handling)

# Features
1. Show Table: Displays the current expense table from exp_page.xlsx.

2. Make an Entry: Allows the user to add a new expense entry with details such as transaction description and amount.

3. Sum of Transactions: Calculates the total sum of transactions within a specified date range.

4. Exit System: Exits the Expense Tracker system

# Usage
Clone the Repository:

```
git clone https://github.com/SakshamDev2005/expense-tracker.git
cd Expense-Tracker/exp-tracker
```

Install Dependencies:

```pip install pandas openpyxl```

Run the Application:

Execute the Python script ```exp_tracker.py```

# File Structure
 - expense_tracker.py: Python script implementing the Expense Tracker functionalities.

 - exp_page.xlsx: Excel file storing the expense data.

# Notes
Ensure that exp_page.xlsx exists in the same directory as expense_tracker.py before running the application.

Any updates or modifications to the expense data will be reflected directly in exp_page.xlsx.
