# Web-Monitor
#coding #task

## Table of contents
* [General info](#general-info)
* [Main funcions](#main-functions)
* [Details](#details)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Program that monitors web sites and reports
their availability. This tool is intended 
as a monitoring tool for web site 
administrators for detecting problems on
theis sites.

## Main functions
* Program reads list of web pages (HTTP URLs)
and corresponding page content requirements 
from configuration file (config.json).
* Program periodically makes an HTTP request 
to each page
* Program verifies that the page content
received from the server matches the content
requirements.  
* Mesures the time it took for the web server
to complete request.  
* Writes a log file (Log.txt) contains: date and 
time of check, checked URL, site status, response time.
* Program runs  HTTP server interface that
shows single HTML page with monitored web sites and 
their last check status.

## Details
* Content requirement and page URL are configurablle by 
setting in the configuration file config.json.  
* Checking period is configurable by setting in configuration
file config.json on via command-line option Set Check Period:
scp :SECONDS:<int>
    
```
python options.py -scp SECONDS
```

* Program writes log file Log.txt. Logfile contains: 
check date and time, checked URLs, their status, 
response times.
* Program distiguish: connection errors, URL errors, 
response errors, invalid content error.

    
## Technologies
Project is created with:
* Python 3.7.1


## Setup

```
pip3 install -r requirements.txt
python app.py
```
