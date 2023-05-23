import webapp2
import os
import urllib
import json
from google.appengine.ext.webapp import template
class MainPage(webapp2.RequestHandler):
    def get(self):
        temp={}
        path=os.path.join(os.path.dirname(__file__),'templates/index.html')
        self.response.out.write(template.render(path,temp))

    def post(self):
        pincode=self.request.get('pincode')
        url="https://api.postalpincode.in/pincode/"+pincode
        data=urllib.urlopen(url).read()
        data=json.load(data)
        status=data[0]['status']

        if status=="Success":
            name=data[0]['PostOffice'][0]['Name']
            region=data[0]['PostOffice'][0]['Region']
            temp={{"name":name,"region":region}}
            path=os.path.join(os.path.dirname(__file__),'templates/results.html')
        
        if status=="Error":
            temp={{"data":data}}
            path=os.path.join(os.path.dirname('templates/error.html'))
            
        self.response.out.write(template.render(path,temp))
app= webapp2.WSGIApplication([('/',MainPage)],debug=True)
