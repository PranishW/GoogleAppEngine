import os
import webapp2
import json
import urllib
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values ={
            "error":""
        }
        path = os.path.join(os.path.dirname(__file__),'templates/index.html')
        self.response.out.write(template.render(path,template_values))

    def post(self):
        try:
            name = self.request.get('name')
            url = 'http://universities.hipolabs.com/search?name='+name
            data = urllib.urlopen(url).read()
            data = json.loads(data)
            data = data[0]
            template_values = {
                "country":data['country'],
                "name":data['name'],
                "web_pages":data['web_pages'][0]
            }
            path = os.path.join(os.path.dirname(__file__),'templates/result.html')
            self.response.out.write(template.render(path,template_values))
        except Exception:
            template_values ={
            "error":"Error, in searching university pls try using appropriate name"
        }
            path = os.path.join(os.path.dirname(__file__),'templates/error.html')
            self.response.out.write(template.render(path,template_values))

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)