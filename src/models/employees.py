import datetime
from google.appengine.ext import db

class Employee(db.Model):
    employee_id = db.IntegerProperty()
    first_name = db.StringProperty()
    last_name = db.StringProperty()
    phone = db.StringProperty()
    email = db.StringProperty()
    address = db.StringProperty()
    postal_code = db.StringProperty()
    city = db.StringProperty()
    province = db.StringProperty()
    country = db.StringProperty()
    start_date = db.DateProperty()
    ending_date = db.DateProperty()
    current_employee = d.BooleanProperty()
    team = db.StringProperty()

# employee = Employee(first_name='Antonio',
#                     last_name='Salieri')

employee.start_date = datetime.datetime.now().date()
employee.current_employee = True

employee.put()