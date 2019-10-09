#!/usr/bin/env python3
import os
import csv

def print_list(list_data, list_type):
    print("\nHere is the listing of {}:".format(list_type))
    for item in list_data:
        print(item)

#set up working directory, file name, full file path
working_dir = 'Automation course\Documents'
file_name = 'customers.csv'
new_file_name = 'new_customers.csv'
my_file = os.path.join('C:\\Users\plaskows\PycharmProjects\Security', working_dir, file_name)
my_new_file = os.path.join('C:\\Users\plaskows\PycharmProjects\Security', working_dir, new_file_name)

#read from a csv file
customer_file = open(my_file)
customer_reader = csv.reader(customer_file)
customer_data = list(customer_reader)
print("\nPassing the reader to list() creates a list of lists:")
print(customer_data)
input("\nPress Enter to continue")
print_list(customer_data, 'customers')
input("\nPress Enter to continue")
print(customer_data[1][1] + ' email: ' + customer_data[1][2])
input("\nPress Enter to continue")
customer_file.close()

#write to csv file
customer_file = open(my_new_file, 'w', newline='')
customer_writer = csv.writer(customer_file)
customer_writer.writerow(['customer_id', 'customer_name', 'customer_email', 'prov_state', 'country'])
customer_writer.writerow(['1', 'Claudia Sand', 'Claudia_Sand@hotmail.com', 'NY', 'US'])
print("\nSuccessfully created new customer data file...")
input("\nPress Enter to continue")
customer_file.close()
