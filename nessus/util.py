# Utility functions
import urllib
import urllib2
import json
import base64
import datetime

def merge_params(target, source):
  params = target
  params.update(source)
  return params
  
def send_request(connection_string, url_params={}, post_params={}):
  url_params['json'] = 1
  url_params = urllib.urlencode(url_params)
  post_params = urllib.urlencode(post_params)
  
  if len(url_params) == 0:
    url = connection_string
  else:
    url = connection_string + '?' + url_params
  response = urllib2.urlopen(url, post_params).read()
  
  return json.loads(response)['reply']['contents']
  
def download_file(connection_string, url_params={}, post_params={}):
  url_params['json'] = 1
  url_params = urllib.urlencode(url_params)
  post_params = urllib.urlencode(post_params)
  
  if len(url_params) == 0:
    url = connection_string
  else:
    url = connection_string + '?' + url_params
  response = urllib2.urlopen(url, post_params).read()
  
  return response
  
def decode_filename(encoded_string):
  full_filename = base64.b64decode(encoded_string)  
  return full_filename.split("|")[1] 

def timestamp_to_date(timestamp):
  return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')  

  
  

  
