import Queue
import os
import socket
import subprocess
import sys
import threading
from datetime import datetime

from auth_scrape import *

MAX_THREADS = 50


def prompt():
    subprocess.call('clear', shell=True)
    print "-" * 60
    print "Please pick an option to proceed"
    print "1. Scan ports of a single host"
    print "2. Scan your current device's ports"
    print "3. Scan ports with a given list"
    print "4. Scan ports from the auth.log"
    print "-" * 60
    option = raw_input("Enter the number of your choice: ")
    if ((int(option) == 1) or (int(option) == 2)):
        indivdual_port_scan()
    elif (int(option) == 3):
        print "Currently Developing"
        sys.exit
    elif (int(option) == 4):
        auth_log_port_scan()
    else:
        sys.exit()


# def file_port_scan():


def auth_log_port_scan():
    subprocess.call('clear', shell=True)
    print "-" * 60
    path = raw_input(
        "Please provide the path to the file for parsing or nothing to read from auth.log in the log folder: ")
    dir = os.path.dirname(__file__)

    if (path == ""):
        path = "input_logs/test.log"
        filename = os.path.join(dir, path)

    ipDict = auth_scrape(filename)

    for line in ipDict:
        ip = ("".join(ipDict[line]))
        port_scan(str(ip))


def indivdual_port_scan():
    subprocess.call('clear', shell=True)
    try:
        remoteServer = raw_input("Enter a remote host to scan (Or nothing to check ports on current system): ")
        print remoteServer
        if (remoteServer == ""):
            remoteServer = socket.getfqdn()
            remoteServerIP = socket.gethostbyname(remoteServer)
        else:
            remoteServerIP = socket.gethostbyname(remoteServer)
    except:
        remoteServer = socket.getfqdn()
        print remoteServer
        remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60

    # Check what time the scan started
    t1 = datetime.now()

    try:
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print 'Scanning Completed in: ', total


def port_scan(ip_address):
    remoteServerIP = socket.gethostbyname(ip_address)

    # Print a nice banner with information on which host we are about to scan
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60

    # Check what time the scan started
    t1 = datetime.now()

    try:
        # for port in range(1, 65535):
        #     print port
        #     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #     result = sock.connect_ex((remoteServerIP, port))
        #     if result == 0:
        #         print "Port {}: 	 Open".format(port)
        #     sock.close()

        scan(ip_address, 0, 65535)

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()
    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
    except socket.error:
        print "Couldn't connect to server"

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print 'Scanning Completed in: ' + total + " For Host" + remoteServerIP


class Scanner(threading.Thread):
    def __init__(self, inq, outq):
        threading.Thread.__init__(self)
        self.setDaemon(1)
        # Queues for (host, port)
        self.inq = inq
        self.outq = outq

    def run(self):
        while 1:
            host, port = self.inq.get()
            sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                # connect to the given host:port
                sd.connect((host, port))
            except socket.error:
                # set the CLOSED flag
                self.outq.put((host, port, 'CLOSED'))
            else:
                self.outq.put((host, port, 'OPEN'))
                sd.close()


def scan(host, start, stop, nthreads=MAX_THREADS):
    toscan = Queue.Queue()
    scanned = Queue.Queue()
    try:
        scanners = [Scanner(toscan, scanned) for i in range(nthreads)]
        for scanner in scanners:
            print scanner
            scanner.start()

        hostports = [(host, port) for port in xrange(start, stop + 1)]
        for hostport in hostports:
            print hostport
            toscan.put(hostport)
    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    results = {}
    for host, port in hostports:
        while (host, port) not in results:
            nhost, nport, nstatus = scanned.get()
            results[(nhost, nport)] = nstatus
        status = results[(host, port)]
        if status <> 'CLOSED':
            print '%s:%d %s' % (host, port, status)


if __name__ == '__main__':
    prompt()
