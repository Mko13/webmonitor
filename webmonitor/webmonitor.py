""" This module includes the functions 
for monitoring and logging the status of the 
websites. Requirements for monitoring are defined
in 'config.ini' file.
"""  

import requests

def checkstatus(url):
    """ Make HTTP request to url. return status code """
    TIMEOUT = 5 # seconds
    try:
        r = requests.get(url, timeout = TIMEOUT)
        r.raise_for_status()
    except requests.exceptions.RequestException as request_error:
        print(request_error)
    except requests.exceptions.HTTPError as error:
        print(error)
    return r.status_code
        #sys.exit(1)
        

