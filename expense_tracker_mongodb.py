
from datetime import datetime
from bson import ObjectId
from ex_db import MONGO_URI
from pymongo import MongoClient
from utils_ex import top, bottom, top1, bottom1, error_handling 

client = MongoClient(MONGO_URI)
db = client["Expense_tracker"]

collection  =db["Expenses"]


def view_all_expense():
    try:
        view = collection.find()
        for doc in view:
            top()
            print(f"ID:{doc['_id']}\nDate:{doc['date']}\nAmount:{doc['amount']}\nCategory:{doc['category']}\nDescription:{doc['description']}")
            bottom()
    except Exception as e :
        error_handling(e)

def add_expense(amount, category, note, date):
    try :
        expense = {
        'date':date, 
        'amount':amount,
        'category':category,
        'description':note
    }
        insert = collection.insert_one(expense)

        if insert.acknowledged :
            top()
            print("Inserted successfully ")
            bottom()
        else :
            top()
            print("Insert operation unsuccessful!")
            bottom()
    except Exception as e :
        error_handling(e)


def view_monthly_expense(date_3):
    try :
        monthly_expense = collection.aggregate([
            {"$addFields": {"month":{"$month":"$date"},
            "year":{"$year":"$date"}}},

            {"$match":{
                "month":date_3.month,
                "year":date_3.year
            }},

            {"$group":{
                "_id":0,
                "total_monthly_expense":{"$sum":"$amount"}
            }}
        ])
        result = list(monthly_expense)
        if result:
            top()
            print(f"Your monthly expense is ${result[0]["total_monthly_expense"]}")
            bottom()
        else:
            top()
            print(f"There is no expense of this month.")
            bottom()

    except Exception as e :
        error_handling(e)     
        

def total_expense():
    try:
        today = datetime.today()
        start = datetime(today.year, today.month, today.day)
        end = datetime(today.year, today.month, today.day+1)
        total = collection.aggregate([{
            "$addFields":{
                "day":{"$dayOfMonth": "$date"},
                "month":{"$month":"$date"},
                "year":{"$year":"$date"},
            }
        },
        {
            "$match":{
                "date":{"$gte":start,
                        "$lte":end}
            }
        },
        {
            "$group":{
                "_id":0,
                "today_expense":{"$sum":"$amount"}
            }
        }
        ])
        result = list(total)

        expenses = collection.find({
            "date":{"$gte":start,"$lte":end}
        })

        top1()
        print("Here is your today's expense")
        bottom1()

        for exp in expenses:
            top()
            print(f"Amount:{exp.get("amount",'N/A')}\nCategory:{exp.get("category",'N/A')}\nDescription:{exp.get("description",'N/A')}")
            bottom()

        if result :
            top1()
            print(f"Your today's total expense is ${result[0]["today_expense"]} ")
            bottom1()
        else:
            top1()
            print(f"There is no expense")
            bottom1()
        
    except Exception as e :
        error_handling(e)

def delete_expense(user_input):
    try :
        delete = collection.delete_one({"_id":ObjectId(user_input)})
        if delete.deleted_count > 0 :
            top()
            print("Deleted successfully")
            bottom()
        else :
            top()
            print("Delete operation Failed!")
            bottom()
    except Exception as e :
        error_handling(e)

def edit(edit_id,amount,category,note,date):
    try :
        update = collection.update_one({"_id":ObjectId(edit_id)},
                                    {"$set":{
                                        "amount":amount,
                                        "category":category,
                                        "description":note,
                                        "date":date
                                    }})
        if update.matched_count == 0:
            top()
            print("No expense found!")
            bottom()
            return 
        
        if update.modified_count > 0:
            top()
            print("Edited successfully")
            bottom()
        else:
            top()
            print("No changes made")
            bottom()

    except Exception as e :
        error_handling(e)

def main() :
    top()
    print("Wecome to Expense Tracker")
    bottom()
    top1()
    print("EXPENSE TRACKER | choose an option ")
    bottom1()
    while True:
        
        print("1. View all expense")
        print("2. Add an expense")
        print("3. View monthly expense ")
        print("4. View total expense")
        print("5. Edit")
        print("6. Delete expense")
        print("7. Exit the app")

        choice = input("choose an option: ")

        match choice :
            case '1':
                view_all_expense()

            case '2':
                amount = int(input("Enter the number of $amount: "))

                category = input("Enter the item name: ")

                note = input("Where are you spending it: ")

                date1= (input("Enter the date(YYYY-MM-DD): "))

                date = datetime.strptime(date1, "%Y-%m-%d")

                add_expense(amount, category, note, date)

            case '3':
                date_2 = input("Enter the month and year(YYYY-MM): ") 
                date_3 = datetime.strptime(date_2, "%Y-%m")
                
                view_monthly_expense(date_3)
                
            case '4':
            
                total_expense()
                
            case '5':
                view_all_expense()
                edit_id = input("Enter the id to edit the expense: ")

                amount = int(input("Enter the number of $amount: "))

                category = input("Enter the item name: ")

                note = input("Where are you spending it: ")

                date1= (input("Enter the date(YYYY-MM-DD): "))

                date = datetime.strptime(date1, "%Y-%m-%d")
                edit(edit_id,amount,category,note,date)

            case '6':
                view_all_expense()

                user_input= input("Enter the id to delete the expense: ")

                delete_expense(user_input)

            case '7':
                exit()

            case _:
                top()
                print("Invalid option! Try again!")
                bottom()



if __name__ == "__main__":
    main()

