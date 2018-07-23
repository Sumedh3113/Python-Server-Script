#!"C:\\Users\\sumed\\AppData\\Local\\Programs\\Python\\Python36-32\\Python.exe"

import cgi

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
	
	
if __name__=='__main__':
	try:
		htmltop()
		print("Hello World") 
		htmltail()
	except:
		cgi.print_exception()