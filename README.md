PyNessusAPI
===

python module for interacting with Nessus servers

Example command line usage
-----

```
  Usage: nessus-client [Options]
  
  Options:
  -h --help                            Help
  -s --server                          Nessus server URL 
                                       (default: https://127.0.0.1:8834) Note: No trailing slash

  -u --username                        Nessus username 
  -p --password                        Nessus password
  --list-reports                       List available reports
  --list-templates                     List scan templates
  --list-scans                         List running scans
  -r --run=[template id]               Run a scan template
  -g --generate-report=[report id]     Generate a report
  -L --generate-last=[num]             Generate last x number of reports
  -f --report-format=[format]          Report format. Valid formats:(nchapter.html, nessusv2, xslt.csv.xsl)
  -o --output-file=[filename]          Output file

```

Example usage from within python
-----

```
from pynessus-api import api
import pprint

# create an instance of the API
a = api.Api()
a.login('https://[ip or hostname of nesuss server]:8834',[username],[password])

reports = a.report_list()
pprint.pprint(reports)

```

Installation 
------------
```
git clone https://github.com/metaevolution/pynessus-api.git pynessus-api
cd pynessus-api
sudo python setup.py install
```

