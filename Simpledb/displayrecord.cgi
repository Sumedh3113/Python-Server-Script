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
	
	
	
def selectPerson(db,cursor):
	sql = "select * from person"
	cursor.execute(sql)
	#fetch the result
	people = cursor.fetchall()
	return people
	
def displaypeople(people):
	print("<table border ='1'>")
	print("<tr>")
	print("<th>ID</th>")
	print("<th>Name</th>")
	print("<th>Lastname</th>")
	print("</tr>")
	for each in people:
		print("<tr>")
		print("<td>{}</td>".format(each[0]))
		print("<td>{}</td>".format(each[1]))
		print("<td>{}</td>".format(each[2]))
		print("</tr>")
	print("<table>")
		
	
	
	
if __name__=='__main__':
	try:
		htmltop()
		db,cursor =connectDB()
		people =selectPerson(db,cursor)
		cursor.close()
		displaypeople(people)
		htmltail()
	except:
		cgi.print_exception()