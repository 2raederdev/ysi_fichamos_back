import datetime
from google.appengine.ext import db

class Employee(db.Model):
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    phone = db.StringProperty()
    email = db.StringProperty()    

# employee = Employee(first_name='Antonio',
#                     last_name='Salieri')

employee.start_date = datetime.datetime.now().date()
employee.current_employee = True

employee.put()