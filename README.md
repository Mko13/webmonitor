# webmonitor

The package wembonitor is a tool for monitoring the status of the web sites.

Features
---------

* Reads a list of urls, and parameters from config.ini file.
* Periodically makes HTTP request to each url. The default interval is 0.0 seconds
  and can be modified by the user in the config.ini file.
* Reports the status of the connection:
    "Page OK",
    "HTTP error",
    "Connect timed out",
    "Connection Error", or
    "Request error."
* Searches specific string ("About us") in the response HTML received from the server.
  Search string can also be specified by the user.
* Measures the total time of the request handling.
* Writes a log file with the format in the file "webmonitor.log":
  DATE, URL, STATUS, RESPONSE TIME, OTHER INFO

  Example:
  DATE: 2019-02-04 02:20:52.145860 | URL: https://yle.fi/uutiset/osasto/news/ | STATUS: [200] Page OK. |
                              RESPONSE TIME: 0:00:00.170717 |  OTHER INFO: includes_expression 'About us': True


Dependencies on external pakages
-----------
*requests
*beautifulsoup4


TO DO
------
* Implement an interface that shows the latest status of the monitored urls.


Things to consider
--------------------
If we wanted to simultaneously monitor the connectivity (and latencies) from multiple geographically distributed locations and collect all the data to a single report that always reflects the current status across all locations, 
in this case, one would have to take into account different time zones, daylight saving time changes, proxies,  restriction on accessibility depending on the location (where the request is made from).
