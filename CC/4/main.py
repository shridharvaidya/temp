import webapp2

class MainPage(webapp2.RequestHandler):
	def get(Self):
		for i in range(1,11):
			m=5*i
			Self.response.out.write("5 x " + str(i) + "=" + str(m) +"<br>")
			
			
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
