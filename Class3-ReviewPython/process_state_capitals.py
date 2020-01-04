import sys
import os
import re


def abortScript():
    print("Error: Invalid script arg params")
    print("Syntax: process_state_capitals.py <column number> <file name>")
    exit(-1)


def isInteger(val: str) -> bool:
    # return val.isdigit()
    try:
        int(val)
        return True
    except:
        return False


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
    if len(args) != 3:
        abortScript()
    command = sys.argv[1]
    file_name = sys.argv[2]
    print("Command: %s" % command)
    print("File Name: %s " % file_name)
    if isFile(file_name) == False:
        print("Invalid file name")
        abortScript()
    return command, file_name


def extract_column(filename: str, col: int):
    print(filename)
    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            print(line.split(",")[col - 1])


def extract_state_by_end_char(filename: str, chr: str):
    print(filename)
    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            if re.match(r"([\w]?[\w\s]+a),([\w\s]+),([-]?\d+.\d+),([-]?\d+.\d+)", line) is not None:
                print(line)


def extract_cws(filename: str, fileout: str):
    print(filename)
    lines = []
    with open(filename, "r") as fp:
        for line in fp:
            line = line.strip()
            if re.match(r"([\w\s]+),([\w]+),([-]?\d+.\d+),([-]?\d+.\d+)", line) is None:
                print(line)
                lines.append(line + "\n")
    with open(fileout, "w") as fw:
        fw.writelines(lines)


def increment_lat_log(filename: str):
    print(filename)
    lines = []
    no = 0
    with open(filename, "r") as fp:
        for line in fp:
            if no == 0:
                no += 1  # skip header
                continue
            line = line.strip()
            fields = line.split(",")
            fields[2] = str(float(fields[2]) + 1.0)
            fields[3] = str(float(fields[3]) + 1.0)
            line = ",".join(fields)
            lines.append(line + "\n")
    with open(filename, "w") as fw:
        fw.writelines(lines)


def main(params: []):
    cmd, filename = validateParams(params)
    if isInteger(cmd) == True:
        column = int(cmd)
        if column < 1 or column > 4:
            print("Invalid column number.  Retry again with valid column number.")
            abortScript()
        print("extract column number")
        extract_column(filename, column)
    elif cmd == "latlon":
        print("increment lat and lon values by 1 and update values in the file")
        increment_lat_log(filename)
    elif cmd == "cws":
        print("extract capital city is not a single word(capitals_with_spaces.csv)")
        extract_cws(filename, "capitals_with_spaces.csv")
    elif re.match(r"(^[a-zA-Z]$)", cmd) is not None:
        print("extract state ending with the letter")
        extract_state_by_end_char(filename, cmd)
    else:
        abortScript()


if __name__ == "__main__":
    main(sys.argv)
