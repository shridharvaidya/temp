import webapp2

class MainPage(webapp2.RequestHandler):
	def get(Self):
		for i in range(5):
			Self.response.out.write("Shridhar<br>")
			Self.response.out.write("33376<br>")
			Self.response.out.write("T190058740<br>")
			Self.response.out.write("<br>")
			
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)			

