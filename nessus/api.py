import time
import urllib2
import urllib
import json
import util
import random

class Api(object):

  def __init__(self):
    self.params = {} 
    self.params['json'] = 1 
    self.token = None
    self.connection_string = None

  def login(self, connection_string, username, password, url_params={}):
    self.connection_string = connection_string
    params = util.merge_params(self.params, url_params)
    url = "%s/login" % (connection_string)
    response = util.send_request(url, params, {'login':username, 'password':password})
    self.token = response['token']
    return response

  def logout(self, url_params={}):
    if self.token:
      token = self.token
    params = util.merge_params(self.params, url_params)
    url = "%s/logout" % (self.connection_string)
    return util.send_request(url, params, {'token':token})

  def report_list(self, url_params={}):
    if self.token:
      token = self.token
    params = util.merge_params(self.params, url_params)
    url = "%s/report/list" % (self.connection_string)
    return util.send_request(url, params, {'token':token})    

  def report_details(self, report, host, url_params={}):
    if self.token:
      token = self.token
    params = util.merge_params(self.params, url_params)
    url = "%s/report/details" % (self.connection_string)
    return util.send_request(url, params, {'token':token,'report':report,'host':host})    

  def file_report_download(self, report, url_params={}):
    if self.token:
      token = self.token
    params = util.merge_params(self.params, url_params)
    url = "%s/file/report/download" % (self.connection_string)
    return util.download_file(url, params, {'token':token,'report':report})        

  def report_format_generate(self, report, format, chapters=None, filters=[], url_params={}):
    if self.token:
      token = self.token
      params = self.params
    for filter in filters:
      util.merge_params(params, filter)
    url = "%s/report/format/generate" % (self.connection_string)  
    if chapters:
      return util.send_request(url, params, {'token':token,'report':report,'format':format,'chapters':chapters})    
    else:
      return util.send_request(url, params, {'token':token,'report':report,'format':format})    
    
  def report_format_status(self, file, url_params={}):
    if self.token:
      token = self.token
    params =  util.merge_params(self.params, url_params)
    url = "%s/report/format/status" % (self.connection_string)      
    return util.send_request(url, params, {'token':token,'file':file})    
    
  def report_format_download(self, file, url_params={}):
    if self.token:
      token = self.token
    params =  util.merge_params(self.params, url_params)
    url = "%s/report/format/download" % (self.connection_string) 
    return util.download_file(url, params, {'token':token,'file':file})    

  def template_list(self, url_params={}):
    if self.token:
      token = self.token
    params = util.merge_params(self.params, url_params)
    url = "%s/scan/template/list2" % (self.connection_string)
    return util.send_request(url, params, {'token':token}) 

  def policy_list(self, url_params={}):
    if self.token:
      token = self.token
    params = util.merge_params(self.params, url_params)
    url = "%s/policy/list/policies" % (self.connection_string)
    return util.send_request(url, params, {'token':token}) 
  
  def scan_list(self, url_params={}):
    if self.token:
      token = self.token
    params = util.merge_params(self.params, url_params)
    url = "%s/scan/list2" % (self.connection_string)
    return util.send_request(url, params, {'token':token}) 
    
  def launch_scan_template(self, template,url_params={}):
    if self.token:
      token = self.token
    params = util.merge_params(self.params, url_params)
    url = "%s/scan/template/launch" % (self.connection_string)
    return util.send_request(url, params, {'token':token,'template':template}) 
  
  def launch_adhoc_scan(self, policy, plugin_id=None, url_params={}):
    if self.token:
      token = self.token
    params = util.merge_params(self.params, url_params)
    url = "%s/scan/new" % (self.connection_string)
    return util.send_request(url, params, {'scan_name':'adhoc_'+random.randint(1,65535),'token':token,'template':template}) 
    
    
if __name__ == "__main__":
  import sys
  
  filters = [
  {'search_type':'and',
   'filter.0.quality':'neq',
   'filter.0.filter':'risk_factor',
   'filter.0.value':'None'}
  ]
  try:
    username = sys.argv[1]
    password = sys.argv[2]
    server = sys.argv[3]
  except:
    print "Usage: %s [Username] [Password] [Nessus Server URL]"
    sys.exit()
  
  a = Auth()
  r = a.login(sys.argv[3], sys.argv[1], sys.argv[2])
  import pprint
  pprint.pprint(r)  

  for report in a.report_list(server)['reports']['report']:
    
    queue = a.report_format_generate(report['name'], 'nchapter.html', 'vuln_by_host;remediations', filters)
    f = open(util.decode_filename(queue['file']), 'wb')
    while 1:
      if a.report_format_status(server,queue['file'])['status'] == 'ready':
        break
      else:
        time.sleep(2)
    f.write(a.report_format_download(queue['file']))
    

  
