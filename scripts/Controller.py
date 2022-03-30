#!/usr/bin/env python3

import argparse
import time
import logging
import json
import os
import re
from Usage import Usage
from UserAgentsManager import UserAgentsManager
from UserRequestsManager import UserRequestsManager
from HttpMethodsManager import HttpMethodsManager

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

class Controller:
    NO_OF_REQUESTS, FREQUENT_USERS, GET_POST_CALL_RATIO = True, True, True

    def __init__(self, log_file, user_requests_analysis, user_agents_analysis, http_get_post_ratio):
        self.log_file = log_file
        self.user_requests_analysis = user_requests_analysis
        self.user_agents_analysis = user_agents_analysis
        self.http_get_post_ratio = http_get_post_ratio
    
    def process(self):
        print("\n********** USET INPUT *************************")
        logging.info("User traffic log file: {} _/".format(self.log_file))
        logging.info("User_requests_analysis: {} _/".format(self.user_requests_analysis))
        logging.info("User_agents_analysis: {} _/".format(self.user_agents_analysis))
        logging.info("Http_get_post_ratio: {} _/".format(self.http_get_post_ratio))
        print("***********************************************\n")
        
        # Part 1: working on finding number of requests by day
        if self.user_requests_analysis:
            user_requests_manager = UserRequestsManager()
            access_request_count = user_requests_manager.fetch_requests_by_day(self.log_file)
            if access_request_count is not None:
              logging.info(" ~~~~ NUMBER OF REQUSTS SERVED BY DAY ~~~~\n")
              print(json.dumps(access_request_count, indent=4))
        
        # Part 2: working on finding top three user agents by day
        if self.user_agents_analysis:
            user_agents_manager = UserAgentsManager()
            frequent_user_agents = user_agents_manager.fetch_frequent_user_agent(self.log_file)
            logging.info(" ~~~~ Three Most Frequent User Agents by day ~~~~\n")
            if frequent_user_agents is not None:
              # print(json.dumps(frequent_user_agents, indent=4))
              top_three_user_agent = user_agents_manager.build_top_three_user_agent(frequent_user_agents)
              print(json.dumps(top_three_user_agent, indent=4))
        
        # Part 3: working on finding ratio between GET and POST call by OS by day
        # TO DO: part 3 will be pushed in next subsequent release ..
        # WORK IN PROGRESS ......
        if self.http_get_post_ratio:
            http_get_post_maanger = HttpMethodsManager()
            get_post_ratio = http_get_post_maanger.fetch_get_post_ratio(self.log_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform an analysis on user web traffic")
    # Command line options for user inputs
    parser.add_argument("-f", "--log_file", help="Specify the web based user traffic log file name with full path", required=True)
    
    # when -a/--all_analysis is used, all analysis will be performed and this overides any specific user command line option selection
    parser.add_argument("-a", "--all_analysis", action="store_true", help="1. Number of user requests served by day, 2. List three most frequent user agents by day, 3. Ratio of GET to POST HTTP method calls by OS by day", default=False)
    
    """
    *** Command line options to perform various user traffic analysis from log file ***
    -ur is user_requests which will count the number of user requests served by day.
    -ua is user_agents which will top three frequent user agents being used by day.
    -gp is http GET and POST method count for each day.
    """ 
    parser.add_argument("-ur", "--user_requests", action="store_true", help="Number of user requests served by day", default=False)
    parser.add_argument("-ua", "--user_agents", action="store_true", help="List three most frequent user agents by day", default=False)
    parser.add_argument("-gp", "--get_post_ratio", action="store_true", help="Ratio of GET to POST HTTP method calls by OS by day", default=False)

    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode", default=False)
    args = parser.parse_args()
    
    if args.verbose:
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

    if args.log_file:
      logging.info("Working on user traffic log file: {}".format(args.log_file))
      if not args.all_analysis:
        if not args.user_requests:
            Controller.NO_OF_REQUESTS = False
        elif args.user_requests:
            logging.info("Working on finding number of requests served by day !")  
      
        if not args.user_agents:
            Controller.FREQUENT_USERS = False
        elif args.user_agents:
            logging.info("Working on finding top three user agents by day !")
      
        if not args.get_post_ratio:
            Controller.GET_POST_CALL_RATIO = False
        elif args.get_post_ratio:
            logging.info("Working on finding GET to POST ratio by OS by day !")
        
        if Controller.NO_OF_REQUESTS is False and Controller.FREQUENT_USERS is False and Controller.GET_POST_CALL_RATIO is False:
            Usage.usage_description()

      elif args.all_analysis:
          Controller.NO_OF_REQUESTS, Controller.FREQUENT_USERS, Controller.GET_POST_CALL_RATIO = True, True, True
          logging.info("Working on all user traffic analysis: \n1. Number of user requests served by day \n2. List three most frequent user agents by day \n3. Ratio of GET to POST HTTP method calls by OS by day")
      
      # start working
      controller = Controller(args.log_file, Controller.NO_OF_REQUESTS, Controller.FREQUENT_USERS, Controller.GET_POST_CALL_RATIO)
      controller.process()

    elif not args.log_file:
      Controller.NO_OF_REQUESTS, Controller.FREQUENT_USERS, Controller.GET_POST_CALL_RATIO = False, False, False
      Usage.usage_description()