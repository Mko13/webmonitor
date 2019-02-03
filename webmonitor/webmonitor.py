""" This module includes the functions
for monitoring and logging the status of the
websites. Requirements for monitoring are defined
in 'config.ini' file.
"""

import re
import sys

import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser

# read configuration parameters
config = ConfigParser()
config.read('config.ini')


def checkstatus(url_addr):
    """ Make HTTP request to url. Return requests.models. Return status,
    and Response object if exists """
    TIMEOUT = 5    # seconds
    try:
        r = requests.get(url_addr, timeout=TIMEOUT)
        r.raise_for_status()
        status = "Page OK."
    except requests.exceptions.HTTPError as http_error:
        status = http_error
    except requests.exceptions.RequestException as request_error:
        status = request_error
        sys.exit(1)
    return None, status


def findstring(content, expression):
    """ Find string expression in the HTML content. Return boolean. """
    s = BeautifulSoup(content, 'html.parser')
    if not s.find_all(string=re.compile(expression)):
        return False
    else:
        return True
    
    
INTERVAL = float(config.get("interval", "request_interval"))