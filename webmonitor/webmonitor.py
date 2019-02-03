""" This module includes the functions 
for monitoring and logging the status of the 
websites. Requirements for monitoring are defined
in 'config.ini' file.
"""  

import requests

def checkstatus(url):
    """ Make HTTP request to url. return status code """
    TIMEOUT = 5
    return requests.get(url, timeout = TIMEOUT)

