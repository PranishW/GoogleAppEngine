import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>Table of 10</h1>')
        for i in range(1,11):
            self.response.write('<h2>10 x '+str(i)+" = "+ str(10*i)+' </h2>')

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)