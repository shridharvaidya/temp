import os
import json
import urllib
import webapp2
#webapp2 includes a number of features that make developing web applications easier, such as improved support for URI routing, session management and localization. The Python 2.7 runtime uses webapp2, and the project is maintained externally to App Engine. It is supported, but not maintained, by Google.
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self): # get method ,  will render index.html file .GET is used to request data from a specified resource.
        template_values = {} 
#When end user sends request to server in the form of data, json and many more things then Server 
# will process on that request and sends back to end user in the form of HTML. 
# This single request and response called as Context.here template values .we dont want any context here 
        path = os.path.join(os.path.dirname(__file__), 'index.html') # take this file-> go to its directory ->attach index.html file
        self.response.out.write(template.render(path, template_values)) # rendering of template =index.html
                                #template from  webapp engine . 2 argument path and context .              
    
    def post(self): #POST is used to send data to a server to create/update a resource.
        pincode = self.request.get('zipCode') # catching that zip code sent at the main page .backend part 
        if not pincode.isnumeric() or not len(pincode)==6:
            template_values = {
                "error" : "Incorrect Pin Code (String / False Code entered)"
            }
            path = os.path.join(os.path.dirname(__file__), 'index.html')
            return self.response.out.write(template.render(path, template_values))
        url = "https://api.postalpincode.in/pincode/"+ pincode # fetching the api .pincode is bought from self.request.get
        data = urllib.urlopen(url).read() # collect data from api in data variable. urllib model is used . open url and collect the data 
        data = json.loads(data) #json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
        #Parsing means analyzing and converting a program into an internal format that a runtime environment can actually run
        post_office = data[0]['PostOffice'][0]['State']
        name = data[0]['PostOffice'][0]['Name']
        block = data[0]['PostOffice'][0]['Block']
        district = data[0]['PostOffice'][0]['District']
        template_values = { # this data will be sent back to user at front end .
            "post_office": post_office,
            "name": name,
            "block": block,
            "district": district
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))
        
#      pipeling is done by wsgi  
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
# wsgi application is residing a request(get or post) at local host or root url then Main page application will handle that request 
