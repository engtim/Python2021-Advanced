import sqlite3

conn = sqlite3.connect('Machine_learning_deleting_entry.db') # Connecting to database
c = conn.cursor() # Creating a cursor

# Deleting entry 6 in the Students table
c.execute("DELETE FROM Students WHERE ID = 6")

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
