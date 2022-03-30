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
       OS_REGEX = re.compile(r'')
       HTTP_METHOD_REGEX = re.compile(r'(?:GET|POST)')
       LOG_ITEMS = re.compile('^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) ([^ ]*) ([^ ]*) \[([^\]]*)\] "([^"]*)" \d+ \d+ "([^"]*)" "([^"]*)"')
       get_post_count_by_os = {}
       STEP = 1
       try:
           if os.path.isfile(log_file):
               with open(log_file, "r") as ACCESS_LOG_FILE:
                   for EACH_REQUEST in ACCESS_LOG_FILE:
                       day = (re.search(DAY_REGEX, EACH_REQUEST)).group()
                       # print(day)
                       days_list = list(set(get_post_count_by_os.keys()))
                       if day not in days_list:
                           get_post_count_by_os[day] = {}
                       log_fields = LOG_ITEMS.findall(EACH_REQUEST)
                       # print(log_fields)
                       print(log_fields[0][6].split(" "))
                       
       except (FileNotFoundError, FileExistsError) as FILE_EXCEPTIONS:
            logging.warning("Something went wrong !!")
            logging.error("File Exception: {}".format(FILE_EXCEPTIONS))
            return None
       except AttributeError as REGEX_EXCEPTION:
            logging.warning("Regex Exception: \n{}".format(REGEX_EXCEPTION))
            logging.error("Couldn't parse access log file !!")
            return None
