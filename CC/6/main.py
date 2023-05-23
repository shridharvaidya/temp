import webapp2

class MainPage(webapp2.RequestHandler):
	def get(Self):
		Self.response.write("<h1>First 8 Elements of the Fibonacci Series:</h1>")
        	Self.response.write("<ul>")
		p=0
		c=1
		for i in range(10):
			Self.response.out.write(str(c)+"<br>")
			temp=c
			c=c+p
			p=temp
			
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
			
		
