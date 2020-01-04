#/usr/bin/env python
import sys
import os
import re
from datetime import datetime

VALID_DATE = r"(\d{1,2}/\d{1,2}/\d{4})"
AM_HOURS = r"([0][0-9]|[1][0-1])"
PM_HOURS = r"([1][2-9]|[2][0-9])"
M2_HOURS = r"(\d+)"
DATE_FORMAT = "%d/%m/%Y"


def abortScript():
    print("Error: Invalid script arg params")
    print("Syntax: process_power_consumption.py <start date> <end date> <AM/PM/2M> <in file name> <out file name>")
    print("Date format: dd/mm/yyyy")
    exit(-1)


def isFile(filename: str) -> bool:
    found = False
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            # print(os.path.join(root, name))
            # print(name)
            if name == filename:
                found = True
    return found


def validateParams(args: []):
    print(args)
    if len(args) < 5 or len(args) > 6:
        abortScript()
    start = args[1]
    end = args[2]
    day = args[3]
    file_in = args[4]
    print("Start Date: %s" % start)
    print("End Date: %s " % end)
    print("Day Part: %s " % day)
    print("Input File: %s " % file_in)
    if re.match(r"^(\d{1,2}/\d{1,2}/\d{4})$", start) is None:
        print("Invalid Start Date")
        abortScript()
    if re.match(r"^(\d{1,2}/\d{1,2}/\d{4})$", end) is None:
        print("Invalid End Date")
        abortScript()
    if day not in ["AM", "PM", "2M"]:
        print("Invalid Day Range")
        abortScript()
    if isFile(file_in) == False:
        print("Invalid Input File")
        abortScript()
    file_out = args[5] if len(args) == 6 else "data_for_date_range.txt"
    print("Output File: %s " % file_out)
    return start, end, day, file_in, file_out


def extract_from_file(file_in: str, file_out: str, start_dt: datetime, end_dt: datetime, hour_regex: str):
    print(file_in)
    with open(file_out, "w") as fw:
        with open(file_in, "r") as fp:
            line = fp.readline()  # skip header
            line = fp.readline()
            while line:
                # line = line.strip()
                match_result = re.match(hour_regex, line)
                if match_result:
                    date_str = match_result.group(1)
                    # print(date_str)
                    date_dt = datetime.strptime(date_str, DATE_FORMAT)
                    # print(date_dt)
                    if start_dt <= date_dt <= end_dt:
                        # print(line)
                        fw.write(line)
                line = fp.readline()


def get_hour_regex(day: str):
    day_regex = ""
    if day == "AM":
        day_regex = AM_HOURS
    elif day == "PM":
        day_regex = PM_HOURS
    else:
        day_regex = M2_HOURS
    hour_regex = rf"{VALID_DATE};{day_regex}:"
    return hour_regex


def main(params: []):
    start, end, day, file_in, file_out = validateParams(params)
    start_dt = datetime.strptime(start, DATE_FORMAT)
    end_dt = datetime.strptime(end, DATE_FORMAT)
    hour_regex = get_hour_regex(day)
    print(hour_regex)
    extract_from_file(file_in, file_out, start_dt, end_dt, hour_regex)


if __name__ == "__main__":
    main(sys.argv)
