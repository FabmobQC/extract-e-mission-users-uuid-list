#!/usr/bin/python
# Script to extract E-mission users' UUIDs before a specific date
# a CSV file for all user

from pymongo import MongoClient
import csv
from datetime import date
from datetime import datetime
import json
import uuid
import sys
import getopt

def main(argv):

    try:
        opts, args = getopt.getopt(argv, "hd:", ["dfile="])
    except getopt.GetoptError:
        print('main.py -d end_interval_date')
        sys.exit(2)

    config_file = open('.env')
    config_data = json.load(config_file)

    client = MongoClient(config_data["url"])
    db = client.Stage_database

    end_inteval_date = ""

    for o, a in opts:
        if o == "-d":
            end_interval_date = a
        else:
            assert False, "unhandled option"

    output = open("users_uuid_list_before_" + str(end_interval_date)[:10], "w")

    users_list = db.Stage_Profiles.find({'update_ts': {'$lte': datetime.strptime(end_interval_date, '%Y-%m-%dT%H:%M:%S.%fZ')}})


    for user in users_list:
        print(user["user_id"])
        output.write(user["user_id"].hex)
        output.write('\n')


if __name__ == "__main__":
    main(sys.argv[1:])
