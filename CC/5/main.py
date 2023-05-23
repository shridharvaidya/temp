import webapp2
class MainPage(webapp2.RequestHandler):
	def get(Self):
		n=1
		while n<11:
			m=10*n
			Self.response.out.write("10 x"+str(n)+"="+str(m)+"<br>")
			n+=1
			
app=webapp2.WSGIApplication([('/',MainPage)],debug=True)
