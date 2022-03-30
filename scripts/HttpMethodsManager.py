#!/usr/bin/env python3
import re
import os

class HttpMethodsManager:
    def __init__(self):
        pass
    
    ''''
    def fetch_get_post_ratio(self, log_file):
       DAY_REGEX = re.compile(r'\d{2}\/\w{1,3}\/\d{4}')
       OS_REGEX = re.compile(r'')
       HTTP_METHOD_REGEX = re.compile(r'(?:GET|POST)')
       get_post_ratio = {}
       try:
           if os.path.exist(log_file):
               with open(log_file, "r") as ACCESS_LOG_FILE:
                   for EACH_REQUEST in ACCESS_LOG_FILE:
                       day = (re.search(DAY_REGEX, EACH_REQUEST)).group()
                       days_list = list(set(get_post_ratio.keys()))
                       if day not in days_list:
                           get_post_ratio[day] = {}
    '''
