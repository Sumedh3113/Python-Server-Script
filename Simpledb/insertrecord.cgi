#!"C:\\Users\\sumed\\AppData\\Local\\Programs\\Python\\Python36-32\\Python.exe"

import cgi
import mysql.connector as conn

def htmltop():
	print("""Content-type:text/html\n\n
			 <!DOCTYPE html>
			 <html>
			 <head lang="en">
			 <meta charset = "utf-8">
			 <title>First Script</title>
			 </head>
			 <body>
			""")
			
			
def htmltail():
	print("""</body>
			 </html>""")
			 
def connectDB():
	#establish connection with database
	db = conn.connect(host="localhost",user="root", password='',db='exampledb')
	cursor =db.cursor()
	return db,cursor
	
def createPersonlist():
	#create list
	people = []
	# add persons in list
	people.append(["Adam","Warlock"])
	people.append(["Andy","Ramse"])
	people.append(["Robert","Sane"])
	return people
	
	
def insertPerson(db,cursor,people):
	for each in people:
		sql = "insert into person(firstname,lastname) values('{0}', '{1}')".format(each[0],each[1])
		cursor.execute(sql)
	db.commit()
	
	
	
if __name__=='__main__':
	try:
		htmltop()
		db,cursor =connectDB()
		people =createPersonlist()
		insertPerson(db,cursor,people)
		htmltail()
	except:
		cgi.print_exception()