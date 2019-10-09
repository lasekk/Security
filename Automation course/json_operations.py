#!/usr/bin/env python3
import os
import json

def print_customers(d_data, data_type, data_col):
    print("\nHere is the listing of {}:".format(data_type))
    for item in d_data:
        print(item[data_col])

#set up working directory, file name, full file path
working_dir = 'Automation course\Documents'
file_name = 'customers.json'
my_file = os.path.join('C:\\Users\plaskows\PycharmProjects\Security', working_dir, file_name)

#read from a json file and print to console
customer_open = open(my_file)
customer_data = json.load(customer_open)
print(type(customer_data))
print(type(customer_data[0]))
print(customer_data)
input("\nPress Enter to continue")

print_customers(customer_data, 'customers', 'customer_name')
input("\nPress Enter to continue")