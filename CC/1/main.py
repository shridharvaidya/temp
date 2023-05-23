import webapp2
class MainPage(webapp2.RequestHandler) :
	def get(self):
		for i in range(5):
			self.response.out.write(" Hello,My name is Shridhar <br>")
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)	
