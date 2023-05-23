import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class PincodeException(Exception):
    pass

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_data = {
            "error":""
        }
        path = os.path.join(os.path.dirname(__file__),'templates/index.html')
        self.response.out.write(template.render(path,template_data))
    
    def post(self):
        pincode = self.request.get('pincode')
        name = self.request.get('Branch Name')
        try:
            if len(pincode) != 6:
                raise PincodeException
            try :
                int(pincode)
            except ValueError:
                template_data = {
                    "error" : "Pincode must be an integer"
                }
                path = os.path.join(os.path.dirname(__file__),'templates/error.html')
                return self.response.out.write(template.render(path,template_data))
        except PincodeException:
            template_data = {
                    "error" : "Pincode must be 6 digit integer"
            }
            path = os.path.join(os.path.dirname(__file__),'templates/error.html')
            return self.response.out.write(template.render(path,template_data))
        url = "https://api.postalpincode.in/pincode/"+str(pincode)
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        Post = data[0]['PostOffice']
        j=0;
        for i in range(0,len(Post)):
            if Post[i]['Name'] == name:
                j=i
        template_data = {
            "Name":Post[j]['Name'],
            "DeliveryStatus":Post[j]['DeliveryStatus'],
            "District":Post[j]['District'],
            "State":Post[j]['State']
        }
        path = os.path.join(os.path.dirname(__file__),'templates/result.html')
        self.response.out.write(template.render(path,template_data))

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
        