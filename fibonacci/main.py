import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        curr = 0
        nex = 1
        self.response.write("Fibonacci Numbers<br>")
        for i in range(0,8):
            self.response.write(str(curr)+" ")
            curr = nex - curr
            nex = nex + curr

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)