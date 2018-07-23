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
	db = conn.connect(host="localhost",user="root", password='')
	cursor =db.cursor()
	return db,cursor
	
def createDB(db,cursor):
	#create database
	sql ="create database exampledb"
	cursor.execute(sql)
	db.commit()
	
def createEntity(db,cursor):
    #use created database
	sql ="use exampledb"
	cursor.execute(sql)
	#create simple entity
	sql = '''create table person
	(personid int not null auto_increment,
	firstname varchar(20) not null,
	lastname varchar(20) not null,
	primary key(personid))'''
	cursor.execute(sql)
	db.commit()
	
if __name__=='__main__':
	try:
		htmltop()
		db,cursor =connectDB()
		createDB(db,cursor)
		createEntity(db,cursor)
		#close connection
		cursor.close()
		htmltail()
	except:
		cgi.print_exception()