#!/usr/bin/python
import requests
import sys


def getCompanyName():
        API_KEY = "at_0T55py8cVr5I1UX1A9fhA1cf6iNsq"

        print("--- MAC address vendor lookup ---")
        #MAC_ADDRESS = input('Enter MAC ADDRESS ')  #"44:38:39:ff:ef:57"
        MAC_ADDRESS = sys.argv[1]
        URL = "https://api.macaddress.io/v1?apiKey={0}&output=json&search={1}".format(API_KEY,MAC_ADDRESS)
        r = requests.get(url = URL)
        data = r.json()
	if data['vendorDetails']['companyName']:
		print ("MAC address: " + sys.argv[1])
		print("CompanyName : " + data['vendorDetails']['companyName'])
	else:
		print("No record found for " + sys.argv[1])

if __name__ == '__main__':
        getCompanyName()
