import re


def auth_scrape(auth_log_path):
    ipDict = {}
    log_path = auth_log_path
    log_file = open(log_path, 'r')
    log_info = log_file.readlines()
    log_file.close()
    index = 0
    ## Insert parsed IP addresses into dictionary
    for line in log_info:
        ip = re.findall('(?:\d{1,3}\.){3}\d{1,3}\d{1,2}', line)
        if ip not in ipDict.values():
            ipDict[index] = ip
            index += 1
    ## Finds any empty strings in the dictionary, and deletes the element
    for x in list(ipDict.keys()):
        if ipDict[x] == []:
            del ipDict[x]
    return ipDict


def write_to_csv(dict, output_file):
    with open(output_file, 'wb') as csv_file:
        for key, value in dict.items():
            csv_file.writelines(str(value))


def get_size_dict(ipDict):
    return len(ipDict)


def get_total_line(auth_log_path):
    line_count = 0
    with open(auth_log_path, 'r') as auth:
        for line in auth:
            line_count += 1
    return line_count
