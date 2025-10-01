# Expense Tracker Pro
**Python + MongoDB CLI project to track daily expenses with CRUD operations, monthly reports, and total expense calculation.**

## Features
- View all expenses
- Add, edit, and delete expenses
- View monthly expense
- View today's total expense
- Error handling for invalid IDs and database issues
- Formatted CLI output for readability

  ## Tech Stack
- **Language:** Python 3.12
- **Database:** MongoDB Atlas
- **Libraries/Modules:**
  - `pymongo`
  - `bson`
  - `datetime`
  - `traceback`

  ## Project Structure
- `expense_tracker_mongodb.py` — Main CLI program  
- `utils_ex.py` — Utility functions (formatting and error handling)    
- `README.md` — Project documentation  
- `requirements.txt` — Required Python libraries

## Setup

1. ### Clone the repository:
    **Github repository:** https://github.com/sej1306kook-ui/Expense_tracker_Mongodb-
      
     Or via terminal
       
   **git clone:** `https://github.com/sej1306kook-ui/Expense_tracker_Mongodb-.git`<br>
   
     `cd Expense_tracker_Mongodb-`
2. ### Install dependencies:
    - `pip install -r requirements.txt`
3. ### Run the project:
    - `python expense_tracker_mongodb.py`

## Usage
**Run the project:**
   `python expense_tracker_mongodb.py`
### Choose an option from the main menu:
1. View all expenses – `See all recorded expenses.`

2. Add an expense – `Enter amount, category, description, and date.`
   
3. View monthly expense – `Enter month and year (YYYY-MM) to see total for that month.`
   
4. View today's total expense – `Shows all expenses recorded today with total amount.`
   
5. Edit an expense – `Provide the ID of the expense to update.`
    
6. Delete an expense – `Provide the ID of the expense to delete.`
    
7. Exit the app – `Quit the program.`

## Real-World Applications

- **Personal Finance Management**: Track daily expenses, monitor spending habits, and plan budget effectively.
  
- **Small Business / Freelancers**: Record business expenses, generate monthly reports, and analyze profit/loss.
  
- **Household / Family Budgeting**: Manage family expenses, monitor monthly spending, and control budgets.
   
- **Event / Project Expense Tracking**: Keep track of event or project-related expenses, update/correct records, and review daily/monthly summaries.
   
- **Educational / Student Use**: Students can track pocket money and daily expenses, and analyze monthly spending patterns.

- **Corporate / Office Expense Management**: Companies can track office expenses like stationery, utilities, travel, and client meetings, with monthly summaries for budget control. 

## License
 **MIT License**

 ## Author 
  **Sejal**
