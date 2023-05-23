import os
import webapp2
from google.appengine.ext.webapp import template
import urllib
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "error":""
        }
        path = os.path.join(os.path.dirname(__file__),'templates/index.html')
        self.response.out.write(template.render(path,template_values))
    def post(self):
        latitude = self.request.get('latitude')
        longitude = self.request.get('longitude')
        try :
            float(latitude)
        except ValueError :
            template_values = {
            "error":"Latitude value must be in decimal value"
            }
            path = os.path.join(os.path.dirname(__file__), 'templates/error.html')
            return self.response.out.write(template.render(path, template_values))
        try :
            float(longitude)
        except ValueError :
            template_values = {
            "error":"Longitude value must be a decimal value"
            }
            path = os.path.join(os.path.dirname(__file__), 'templates/error.html')
            return self.response.out.write(template.render(path, template_values))
        url = "https://api.open-meteo.com/v1/forecast/?latitude="+latitude+"&longitude="+longitude+"&current_weather=true"
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        current_weather = data['current_weather']
        day = ''
        if(current_weather['is_day']==0):
            day = 'Night'
        else :
            day = 'Day'
        template_values = {
            "temperature" : current_weather['temperature'],
            "windspeed" : current_weather['windspeed'],
            "winddirection" : current_weather['winddirection'],
            "day" : day
        }
        path = os.path.join(os.path.dirname(__file__),'templates/result.html')
        self.response.out.write(template.render(path,template_values))

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)