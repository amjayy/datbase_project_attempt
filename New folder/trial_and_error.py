import sqlite3

db_conn = sqlite3.connect('customer.db')

c = db_conn.cursor()

db_conn.execute("CREATE TABLE IF NOT EXISTS Customer (Fname VARCHAR(15),Lname VARCHAR(15),Email,Points INT(2)")

db_conn.commit()

fname = input('Please enter your first name:')
lname = input('Please enter your last name:')
email = input('Please enter your email:')
points= input('How many points do you want:')

#def reward_section():
   # print("Thanks for the infomation! Have you shopped with us before?")

    #choice = input("> ")



db_conn.execute("INSERT INTO Customer VALUES('" + fname + "','" + lname + " ', "' + email+ ' ", ' " + points+ " ');")

db_conn.commit()

rows = c.execute("SELECT * FROM Customers;")

for row in rows:
    print(row)


