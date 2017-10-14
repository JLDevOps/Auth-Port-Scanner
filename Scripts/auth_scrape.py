import re


class auth_scrape():
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
