import sqlite3

conn = sqlite3.connect('Machine_Learning_table_updating.db') # Connecting to database
c = conn.cursor() # Creating a cursor


# Updating Records
c.execute("""UPDATE Courses SET Coursename = 'AWS Foundations'
			WHERE ID = '8'
	""")


# Adding new course
new_course = ('10','Introduction to Statistics'),
					

c.executemany("INSERT INTO Courses VALUES (?,?)", new_course)

#Querying database and displaying in terminal 
c.execute("""SELECT Students.ID,
					Students.Fname,
					Students.Lname,
					Students.Country,
					Students.City,
					Students.Continent,
			Courses.Coursename FROM Students, Courses""")

items = c.fetchall()

for item in items:
	print(item)


conn.commit() #committing command
