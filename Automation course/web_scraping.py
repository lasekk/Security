#!/usr/bin/env python3
#import pip.internal as pip
#package_names = ['requests', 'beautifulsoup4']
#pip.main(['install'] + package_names + ['--upgrade'] + ['--quiet'])
import requests
import bs4

def print_list(list_data, list_type):
    print("\nHere is the listing of {}:".format(list_type))
    for item in list_data:
        print(item)

# Download web page - get response object
resp = requests.get('https://www.gutenberg.org/catalog/')
try:
    resp.raise_for_status()
except Exception as exc:
    print('Seems there was a problem: %s' % (exc))
print("\nYou should see '200' status code:")
print(resp.status_code)
input("\nPress Enter to continue")

# Create a beatifulsoup object from the text attribute of the response object
gut_soup = bs4.BeautifulSoup(resp.text, "html.parser")

# Pull all css elements named <input> that have a name attribute with any value
elements = gut_soup.select('input[name]')
print("\nThere are {} elements of type '<input>[name]'".format(len(elements)))
print("...and here they are:")

for item in elements:
    print(item)
input("\nPress Enter to continue")

print("\nCheck the 'class' of one of the elements:")
print(type(elements[2]))
print("\nExamine the elements' attributes:")
for item in elements:
    print(item.attrs)

input("\nPress Enter to continue")


