import webapp2

class MainPage(webapp2.RequestHandler):
	def get(Self):
		n=10
		while n > 0 :
			Self.response.out.write(" T190058740<br>")
			Self.response.out.write(" Information technology<br>")
			Self.response.out.write(" <br>")
			n-=1
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)			
			
