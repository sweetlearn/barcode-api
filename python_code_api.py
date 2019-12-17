# PYTHON 3

import urllib.request
import json
import pprint

api_key = "ENTER_YOUR_API_KEY_HERE"
url = "https://api.barcodelookup.com/v2/products?barcode=077341125112&formatted=y&key=" + api_key

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

barcode = data["products"][0]["barcode_number"]
print ("Barcode Number: ", barcode, "\n")

name = data["products"][0]["product_name"]
print ("Product Name: ", name, "\n")

print ("Entire Response:")
pprint.pprint(data)


# PYTHON 2

import urllib
import json
import pprint

api_key = "ENTER_YOUR_API_KEY_HERE"
url = "https://api.barcodelookup.com/v2/products?barcode=077341125112&formatted=y&key=" + api_key

response = urllib.urlopen(url)
data = json.loads(response.read())

barcode = data["products"][0]["barcode_number"]
print "Barcode Number: ", barcode, "\n"

name = data["products"][0]["product_name"]
print "Product Name: ", name, "\n"

print "Entire Response:"
pprint.pprint(data)