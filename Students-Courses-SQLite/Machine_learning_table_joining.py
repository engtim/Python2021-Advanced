import sqlite3

conn = sqlite3.connect('Machine_Learning_table_joining.db') # Connecting to database
c = conn.cursor() # Creating a cursor


c.execute("""SELECT Students.ID,
					Students.Fname,
					Students.Lname,
					Students.Country,
					Students.City,
					Students.Continent,
			Courses.Coursename FROM Students, Courses""")


for i in c:
	print(i)


	conn.commit() #committing command
