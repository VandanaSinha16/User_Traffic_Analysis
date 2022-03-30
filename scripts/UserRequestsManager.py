#!/usr/bin/env python3

from ipaddress import ip_address
import logging
import re
import os
import sys
from collections import Counter
from telnetlib import IP

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

class UserRequestsManager:
    def __init__(self):
        pass

    def fetch_requests_by_day(self, log_file):
        IP_REGEX = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        DAY_REGEX = re.compile(r'\d{2}\/\w{1,3}\/\d{4}')
        access_request_count = {}
        try:
          if os.path.isfile(log_file):
            with open(log_file, "r") as ACCESS_LOG_FILE:
              for EACH_REQUEST in ACCESS_LOG_FILE:
                day = (re.search(DAY_REGEX, EACH_REQUEST)).group()
                days_list = list(set(access_request_count.keys()))
                if day not in days_list:
                  access_request_count[day] = {}
                IP_ADDRESS = re.search(IP_REGEX, EACH_REQUEST).group(0)
                if IP_ADDRESS not in list(set(access_request_count[day].keys())):
                  CURRENT_COUNTER = 1
                  access_request_count[day][IP_ADDRESS] = CURRENT_COUNTER
                elif IP_ADDRESS in list(set(access_request_count[day].keys())):
                  CURRENT_COUNTER = access_request_count[day][IP_ADDRESS] + 1
                  access_request_count[day][IP_ADDRESS] = CURRENT_COUNTER
            return access_request_count
          elif not os.path.isfile(log_file):
            logging.error("Log file: {} not found !!!".format(log_file))
            sys.exit(1)
        except (FileNotFoundError, FileExistsError) as FILE_EXCEPTIONS:
            logging.warning("Something went wrong !!")
            logging.error("File Exception: {}".format(FILE_EXCEPTIONS))
            return None
        except AttributeError as REGEX_EXCEPTION:
            logging.warning("Regex Exception: \n{}".format(REGEX_EXCEPTION))
            logging.error("Couldn't parse access log file !!")
            return None