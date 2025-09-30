# Expense Tracker Pro
Python + MongoDB CLI project to track daily expenses with CRUD operations, monthly reports, and total expense calculation.

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
**Clone the repository:**  
  - git clone: https://github.com/sej1306kook-ui/Expense_tracker_Mongodb-
- **Install dependencies:**
`pip install -r requirements.txt`
- **Run the project:**
`python main.py`

## Usage
**Run the project:**
   `python main.py`
### Choose an option from the main menu:
- View all expenses – `See all recorded expenses.`
- Add an expense – `Enter amount, category, description, and date.`
- View monthly expense – `Enter month and year (YYYY-MM) to see total for that month.`
- View today's total expense – `Shows all expenses recorded today with total amount.`
- Edit an expense – `Provide the ID of the expense to update.`
- Delete an expense – `Provide the ID of the expense to delete.`
- Exit the app – `Quit the program.`

## License
 **MIT License**

 ## Author 
  **Sejal**
