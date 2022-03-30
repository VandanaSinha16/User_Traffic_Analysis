#!/usr/bin/env python3
import re
import os
import sys
from collections import Counter
import logging
import itertools

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

class UserAgentsManager:
    def __init__(self):
        pass
    

    def build_top_three_user_agent(self, frequent_user_agents):
      """
      build_top_three_user_agent:
      // Method sort the main user agent count data and return only top three frequently used user agents to user
      """
      TOP_THREE = 3
      for each_day in frequent_user_agents.keys():
        user_agent_counts = frequent_user_agents[each_day]
        sorted_user_agent_counts = {k: v for k, v in sorted(user_agent_counts.items(), reverse=True, key=lambda item: item[1])}
        sorted_user_agent_counts = dict(itertools.islice(sorted_user_agent_counts.items(), TOP_THREE)) 
        frequent_user_agents[each_day] = sorted_user_agent_counts
      return frequent_user_agents

    def fetch_frequent_user_agent(self, log_file):
        """
        fetch_frequent_user_agent:
        Method to process the user traffic log file and build json data which consist of users agents and their frequency 
        of incoming request by each day
        """
        DAY_REGEX = re.compile(r'\d{2}\/\w{1,3}\/\d{4}')
        LOG_ITEMS = re.compile('^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) ([^ ]*) ([^ ]*) \[([^\]]*)\] "([^"]*)" \d+ \d+ "([^"]*)" "([^"]*)"')
        user_agent_count = {}
        STEP = 1
        try:
          if os.path.isfile(log_file):
            with open(log_file, "r") as ACCESS_LOG_FILE:
              for EACH_REQUEST in ACCESS_LOG_FILE:
                day = (re.search(DAY_REGEX, EACH_REQUEST)).group()
                days_list = list(set(user_agent_count.keys()))
                if day not in days_list:
                  user_agent_count[day] = {}
                log_fields = LOG_ITEMS.findall(EACH_REQUEST)
                user_agent = (log_fields[0][6]).split(" ")[0]
                if user_agent not in list(set(user_agent_count[day].keys())):
                  CURRENT_COUNTER = STEP
                  user_agent_count[day][user_agent] = CURRENT_COUNTER
                elif user_agent in list(set(user_agent_count[day].keys())):
                  CURRENT_COUNTER = user_agent_count[day][user_agent] + STEP
                  user_agent_count[day][user_agent] = CURRENT_COUNTER
            return user_agent_count
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
