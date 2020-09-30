#!usr/bin/env python

# this will find hidden directories within a specified wordlist

import requests
import optparse


def get_arg():
    parser = optparse.OptionParser()
    parser.add_option("-h", dest="host")
    (options, arguments) = parser.parse_args()
    if not options.host:
        parser.error("specify the host in the form of domain.com -h")
    else:
        return options

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

def get_subdomains(host):
    with open("/root/Downloads/subdomains.list", "r") as word_list:
        for line in word_list:
            word = line.strip()
            test_url = word + "." + host
            response = request(test_url)
            if response:
                print("[+]Subdomain discovered --> " + test_url)

def get_url_directory(host):
    with open("/root/Downloads/common.txt", "r") as common_list:
        for line in common_list:
            url = line.strip()
            test_dir = host + "/" + url
            response = request(test_dir)
            if response:
                print("[+]URL directory discovered --> " + test_dir)

options = get_arg()
get_subdomains(options.host)
get_url_directory(options.host)