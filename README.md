# Auth-Port-Scanner
[![Build Status](https://travis-ci.org/JLDevOps/Auth-Port-Scanner.svg?branch=master)](https://travis-ci.org/JLDevOps/Auth-Port-Scanner)

This python script scrapes the auth.log file on your server, and finds any unauthorized IP addresses or failed authentications IP addresses.  It will log the information into a csv file, and then conduct a reverse port scan on their IP address. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need 
1. Python 2.*
2. PIP (Python Install Packages) - [Link](https://pip.pypa.io/en/stable/installing/)

### Installing

A requirements.txt file has been provided for the installation of any necessary python packages onto your device.

```pip install -r requirements.txt```

## How Do I

These sections below will provide a detailed look on using the functions of the scripts.

### Port Scanning

For just port scanning without a given list, the command is:

```python auth_port_scanner.py```

You will be given two options:
1. Scan your current device's ports
2. Scan a device's port with a given IP address.

## Authors

* **Jimmy Le** - [JLDevops](https://github.com/jldevops)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
