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
	
	
	
def getPerson(db,cursor):
	sql = "select * from person"
	cursor.execute(sql)
	#fetch the result
	people = cursor.fetchall()
	return people

def createDropdown(people):
	print(""" <select name = "drop"> """)
	for persons in people:
		print(""" <option value ="{0}">{1} {2}</option> """.format(persons[0],persons[1],persons[2]))
	print(""" </select> <br>""")
	
def createradio(people):
	for persons in people:
		print(""" <input type = "radio" name="rbutton" value ="{0}" /> {1} {2}""".format(persons[0],persons[1],persons[2]))
		print(""" <br>""")
		
def createcheckbox(people):
	for persons in people:
		print(""" <input type = "checkbox" name="cbox" value ="{0}" /> {1} {2}""".format(persons[0],persons[1],persons[2]))
		print(""" <br>""")

		
def createtestform(people):
	print(""" <form method="post" action="processform.cgi"> """)
	createDropdown(people)
	createradio(people)
	createcheckbox(people)
	print(""" <input type="submit" name= "submittest" value="Submit"> """)
	print(""" </form>""")
	
	
	
	
if __name__=='__main__':
	try:
		htmltop()
		db,cursor =connectDB()
		people = getPerson(db,cursor)
		cursor.close()
		createtestform(people)
		htmltail()
	except:
		cgi.print_exception()