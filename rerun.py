import sqlite3 
from validate_email import validate_email
conn = sqlite3.connect('amber.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS amber(
                first text,
                last text,
                points integer,
                email text
                   )""")
#commits current transaction and changes
c.execute("INSERT INTO amber VALUES('Horatio', 'Caine', 456, 'hcaine@dustymail.com')")
c.execute("INSERT INTO amber VALUES('Dave', 'Folkson', 58600, 'dfolkson@dustymail.com')")
c.execute("INSERT INTO amber VALUES('Callie', 'Dusquene', 78, 'caldusquene@dustymail.com')")
c.execute("INSERT INTO amber VALUES('Kimberly', 'Vaughn', 100,'kimvee@dustymail.com' )")
c.execute("INSERT INTO amber VALUES('Luke', 'Dennison', 325, 'uncleluke@dustymail.com')")
conn.commit()
def returning_email(email):
        email = validate_email(email)
        return email
def new_email(email):
        email = validate_email(input('example@example.com'))
        return email
    
def add_customer_points(customer_points, is_existing):
    if is_existing:
        customer_points += 50
        print("Welcome back! Here are 50 points for you shopping with us today")
    else:
        customer_points += 10
        print("Hello!For being a new customer. You get 10 new points.")
    return is_existing
def first_name(f_name):
    f_name=''
    if f_name.isnumeric():
         print("Letters only.Do not use numbers")
    elif():
        return f_name
    
def last_name(l_name):
    l_name = ''
    if l_name.isnumeric():
       print("Letters only.Do not use numbers.") 
    elif():
        return l_name

def show_users_admin():
    print("Hello administrator.Please enter your pin.")
    pin = input("")
    if pin == "3930":
        c.execute("SELECT * FROM customers")
        print(c.fetchall())
    else:
        ("The authorities have been alerted. Goodbye thief")
           

is_existing= 300
customer_points= 50
def enter_store():
    print("Welcome to Dusty Mart.")
    store = input("Are you a returning customer? Y/N/Admin?:").lower()
    if store == "y":
        email = returning_email(input("Excellent! Please enter your email"))
        add_customer_points(customer_points, is_existing)
    if store == "n":
        print("No worrries! Let's get you set up.")
        fname = first_name(input("Please enter your first name."))
        lname = last_name(input("Please enter your last name."))
        new_email = validate_email(input("Excellent! Please enter your email"))
        customer_points = add_customer_points()
    if store =="admin":
        show_users_admin()
    else:
        ("Get some help.Goodbye.")
        
   # c.execute("INSERT INTO customers VALUES(?, ?, ?, ?)", (first_name, last_name,customer_points, new_email))    
    
#allows to excute some sql commands

#create customer table that holds first, name,last name, and points
#c for the cursor we've created
#c.execute("""CREATE TABLE IF NOT EXISTS amber(
#                  first text,
 #                 last text,
 #                 points integer
  #                email text
   #               )""")
#commits current transaction and changes
#c.execute("INSERT INTO amber VALUES('Horatio', 'Caine', 456, 'hcaine@dustymail.com')")
#c.execute("INSERT INTO amber VALUES('Dave', 'Folkson', 58600, 'dfolkson@dustymail.com')")
#c.execute("INSERT INTO amber VALUES('Callie', 'Dusquene', 78, 'caldusquene@dustymail.com')")
#c.execute("INSERT INTO amber VALUES('Kimberly', 'Vaughn', 100,'kimvee@dustymail.com' )")
#c.execute("INSERT INTO amber VALUES('Luke', 'Dennison', 325, 'uncleluke@dustymail.com')")
#conn.commit()
   
        
 
enter_store()
conn.commit()
conn.close()
