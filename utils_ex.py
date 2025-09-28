from bson.errors import InvalidId
from pymongo.errors  import PyMongoError
import traceback


def top():
    print("\n"+"*"*100)

def bottom():
    print("*"*100+"\n")  

def top1():
    print("\n"+"="*100)
    
def bottom1():
    print("="*100+"\n")


def error_handling(err):
    if isinstance(err, InvalidId):
        top()
        print("Invalid Id! Please enter a valid Id")
        bottom()
    elif isinstance(err, PyMongoError):
        top()
        print(f"Database Error: {err}")
        bottom()
    else:
        top()
        print(f"unexpected Error: {err}")
        traceback.print_exc()
        bottom()
