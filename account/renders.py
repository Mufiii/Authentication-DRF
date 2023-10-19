# Custom renderers are used to control how data is rendered into a response format (in this case, JSON) for your API endpoints. They allow you to customize the format and structure of the response data.


from rest_framework import renderers
import json


class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, render_context=None):
      
      response = ''
      if 'ErrorDetail' in str(data):
          response = json.dumps({'errors':data})
      else:
          response = json.dumps(data)
          
      return response
    
"""

The purpose of this custom renderer is to modify the response format when certain error conditions are met. If the response data contains 'ErrorDetail,' it wraps it in an 'errors' dictionary, presumably to standardize the error format. Otherwise, it converts the data to JSON as usual.

"""