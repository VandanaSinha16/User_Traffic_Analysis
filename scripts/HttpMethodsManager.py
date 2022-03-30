#!/usr/bin/env python3
import re
import os
import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

class HttpMethodsManager:
    def __init__(self):
        pass
    
    def fetch_get_post_ratio(self, log_file):
       DAY_REGEX = re.compile(r'\d{2}\/\w{1,3}\/\d{4}')
       OS_REGEX = re.compile(r'(Windows|Linux|Android|Macintosh|iphone)')
       HTTP_METHOD_REGEX = re.compile(r'(?:GET|POST)')
       LOG_ITEMS = re.compile('^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) ([^ ]*) ([^ ]*) \[([^\]]*)\] "([^"]*)" \d+ \d+ "([^"]*)" "([^"]*)"')
       get_post_count_by_os = {}
       STEP = 1
       INITIALIZE = 0
       try:
           if os.path.isfile(log_file):
               with open(log_file, "r") as ACCESS_LOG_FILE:
                   for EACH_REQUEST in ACCESS_LOG_FILE:
                       day = (re.search(DAY_REGEX, EACH_REQUEST)).group()
                       days_list = list(set(get_post_count_by_os.keys()))
                       if day not in days_list:
                           get_post_count_by_os[day] = {}
                       log_fields = LOG_ITEMS.findall(EACH_REQUEST)
                       if re.search(OS_REGEX, log_fields[0][6]):
                           OS = re.search(OS_REGEX, log_fields[0][6]).group()
                       elif re.search(OS_REGEX, log_fields[0][6]) is None:
                           OS = "Unknown_OS"

                       if OS not in list(set(get_post_count_by_os[day].keys())):
                           get_post_count_by_os[day][OS] = {}
                           get_post_count_by_os[day][OS]['GET'] = INITIALIZE
                           get_post_count_by_os[day][OS]['POST'] = INITIALIZE
                       elif OS in list(set(get_post_count_by_os[day].keys())):
                           if re.search(HTTP_METHOD_REGEX, log_fields[0][4]):
                               http_method = re.search(HTTP_METHOD_REGEX, log_fields[0][4]).group()
                               if http_method == 'GET':
                                 get_post_count_by_os[day][OS]['GET'] = get_post_count_by_os[day][OS]['GET'] + STEP
                               elif http_method == 'POST':
                                 get_post_count_by_os[day][OS]['POST'] = get_post_count_by_os[day][OS]['POST'] + STEP
                           elif re.search(HTTP_METHOD_REGEX, log_fields[0][4]) is None:
                               logging.warning("Failed to parse HTTP method !!")
                               logging.debug("Log fields: {}".format(log_fields[0]))
                               logging.debug("HTTP method filed: {}".format(log_fields[0][4]))  

                   return get_post_count_by_os                            
       except (FileNotFoundError, FileExistsError) as FILE_EXCEPTIONS:
            logging.warning("Something went wrong !!")
            logging.error("File Exception: {}".format(FILE_EXCEPTIONS))
            return None
       except AttributeError as REGEX_EXCEPTION:
            logging.warning("Regex Exception: \n{}".format(REGEX_EXCEPTION))
            logging.error("Couldn't parse access log file !!")
            return None
