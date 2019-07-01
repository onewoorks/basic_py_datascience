from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.test 

employee = db.employee
employee_detail = {
    'Name' : 'Raj Kumar',
    'Address' : 'Sears Steer, NZ',
    'Age' : '42'
}

result = employee.insert_one(employee_detail)
query_result = employee.find_one({'Age':'42'})
pprint(query_result)