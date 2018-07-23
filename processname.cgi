#!"C:\\Users\\sumed\\AppData\\Local\\Programs\\Python\\Python36-32\\Python.exe"

import cgi
import cgitb
cgitb.enable()


def htmltop():
	print("""Content-type:text/html\n\n
			 <!DOCTYPE html>
			 <html>
			 <head lang="en">
			 <meta charset = "utf-8">
			 <title>Process name Script</title>
			 </head>
			 <body>
			""")
			
def getData():
	formData = cgi.FieldStorage()
	firstName = formData.getvalue('firstname')
	firstName1 = formData.getvalue('datef')
	firstName2 = formData.getvalue('emailf')
	return firstName,firstName1,firstName2

			
def htmltail():
	print("""</body>
			 </html>""")
	
	
if __name__=='__main__':
	try:
		htmltop()
		firstName,firstName1,firstName2 = getData()
		print("Hello {}  <br> Date is: {} <br>  Email is: {}".format(firstName,firstName1,firstName2)) 
		htmltail()
	except:
		cgi.print_exception()