import sqlite3

conn = sqlite3.connect('Machine_Learning.db') # Connecting to database
c = conn.cursor() # Creating a cursor

# Creating Table 1: Students
c.execute("""CREATE TABLE Students (
			ID INTEGER, 
			Fname TEXT, 
			Lname TEXT, 
			Country TEXT, 
			City TEXT, 
			Continent TEXT, 
			Course TEXT
		)""")

# Table one tuples
table_one = [
					('1','Nicholas','Okello','Kenya','Nairobi','Africa','Advanced Python'),
					('2','Tim','Kabugi','Kenya','Nairobi','Africa','Advanced Python'),
					('3','John','Weru','Kenya','Nairobi','Africa','Advanced Python'),
					('4','Darik','Olal','Kenya','Nairobi','Africa','Advanced Python'),
					('5','Esther','Wambui','Kenya','Nairobi','Africa','Advanced Python'),
					('6','George','Ndede','USA','Dallas','N.America','Artificial Intelligence'),
				]
c.executemany("INSERT INTO Students VALUES (?,?,?,?,?,?,?)", table_one)

# Creating Table 2: Courses
c.execute("""CREATE TABLE Courses (
			ID INTEGER,  
			Coursename TEXT
		)""")

# Table two tuples
table_two = [
					('1','Advanced Python'),
					('2','Machine Learning'),
					('3','Introduction Data Science'),
					('4','Artificial Intelligence'),
					('5','Introduction Python'),
					('6','Database Management'),
					('7','Intro to Linux Administration'),
					('8','Intro to AWS Foundations'),
					('9','Python System Administration'),
					
				]
c.executemany("INSERT INTO Courses VALUES (?,?)", table_two)

conn.commit() #committing command

