""" This module includes the functions
for monitoring and logging the status of the
websites. Requirements for monitoring are defined
in 'config.ini' file.
"""

import datetime
import re
import time
from configparser import ConfigParser

import requests
from bs4 import BeautifulSoup

# read configuration parameters
config = ConfigParser()
config.read('config.ini')


def checkstatus(url_addr):
    """ Make HTTP request to url. Return status,
    and Response object if exists """
    TIMEOUT = 5    # seconds
    try:
        r = requests.get(url_addr, timeout=TIMEOUT)
        r.raise_for_status()
        status = "Page OK."
        return r, status
    except requests.exceptions.HTTPError:
        status = "HTTP error."
    except requests.exceptions.ConnectTimeout:
        status = "Connect timed out."
    except requests.exceptions.ConnectionError:
        status = "Connection Error."
    except requests.exceptions.RequestException:
        status = "Request error."
    return None, status


def findstring(content, expression):
    """ Find string expression in the HTML content. Return boolean. """
    s = BeautifulSoup(content, 'html.parser')
    if s.find_all(string=re.compile(expression)):
        return True
    else:
        return False


# Alternatively, logging module can be used.
def writelog(url_addr):
    """ Write the status of each webpage in a logfile """

    response, status = checkstatus(url_addr)

    requirement, _expression = config.items('requirements')[0][:]
    expression = _expression[1:-1]  # remove extra parenthesis

    if not response:
        response_code = "None"
        result = "None"
        time_elapsed = "None"
    else:
        response_code = response.status_code
        result = findstring(response.text, expression)
        time_elapsed = response.elapsed

    with open("webmonitor.log", "a+") as logfile:
        logfile.write("DATE: {} | URL: {} | STATUS: [{}] {} | RESPONSE TIME: {} |\
                        OTHER INFO: {} '{}': {} \n"
                        .format(datetime.datetime.now(),
                                url_addr, response_code, status, time_elapsed,
                                requirement, expression, result))


INTERVAL = float(config.get("interval", "request_interval"))


def start(interval=INTERVAL):
    for url_item in config.items("urls"):
        url = url_item[1]
        print("Checking {} " .format(url))
        writelog(url)
    print("-----------------------------------")
    time.sleep(interval)


if __name__ == "__main__":
    while True:
        start()
