#!/usr/bin/env python3
import os
import xml.etree.ElementTree as et



#set up working directory, file name, full file path
working_dir = 'Automation course\Documents'
file_name = 'customers.xml'
my_file = os.path.join('C:\\Users\plaskows\PycharmProjects\Security', working_dir, file_name)

#read from a xml file and print to console
tree = et.parse(my_file)
root = tree.getroot()
print("\nThe root tag is:")
print(root.tag)
input("\nPress Enter to continue")

print("\nList the tag and attrib for children nodes")
for child in root:
    print(child.tag, child.attrib)

input("\nPress Enter to continue")

print("\n\nList each customer, along with their country")
for customer in root.findall('customer'):
    country = customer.find('country').text
    name = customer.get('name')
    print(name + ': ', country)

input("\nPress Enter to continue")