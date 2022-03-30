#!/usr/bin/env python3

from cmath import log
import logging
import sys

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

class Usage:
    def __init__(self):
        pass

    @staticmethod
    def usage_description():
        print("\n !!!!!! BAD USER INPUT !!!!!\n")
        print("~~~ user traffic analysis usage ~~~~~\n")
        print("Trigger all user traffic analysis:\n")
        print("python3 /opt/user_traffic_analysis/scripts/Controller.py -f/--log_file <LOG_FILE_FULL_PATH> -a/--all_analysis")
        print("\n[-f/--log_file] represnts log file name and -a/--all_analysis will trigger all three analysis:\n")
        print("1. Number of user requests served by day \n2. List three most frequent user agents by day \n3. Ratio of GET to POST HTTP method calls by OS by day")
        print("\n****** How to trigger a specific analysis using cmd line options ********")
        print("Options:\n")
        print("[-ur]: Find number of user requests served by day ")
        print("[-ua]: List three most frequent user agents by day ")
        print("[-gp]: Find Ratio of GET to POST HTTP method calls by OS by day\n")
        print("python3 /opt/user_traffic_analysis/scripts/Controller.py  -f/--log_file <LOG_FILE_FULL_PATH> -ur/--user_requests")
        print("python3 /opt/user_traffic_analysis/scripts/Controller.py  -f/--log_file <LOG_FILE_FULL_PATH> -ua/--user_agents")
        print("python3 /opt/user_traffic_analysis/scripts/Controller.py  -f/--log_file <LOG_FILE_FULL_PATH> -gp/--get_post_ratio")
        print("\nplease read the official documenation README.md for more detailed information about the tool")
        sys.exit(1)