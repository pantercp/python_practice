# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:52:24 2022

@author: Ronaldo
"""

import csv
import os

source_dir = os.getcwd()

'''
READS DOC AND FORMATS EACH ROW AS A LIST
'''
# # Create a reader of the file 
# exampleFile = open(source_dir+r'\git\test-g.tsv')
# exampleReader = csv.reader(exampleFile)
# # Create a list of lists and store as a variable
# exampleData = list(exampleReader)
# exampleData

'''
READS DOCS IN A FOR LOOP
'''
# exampleFile = open(source_dir+r'\objectives.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
    
'''
READ ROWS IN DOC BUT IGNORE THE HEADER
'''
# with open(source_dir+file_name, 'r', newline='') as read_obj:
#     reader = csv.reader(read_obj)
#     for row in reader:
#         if reader.line_num == 1:
#             continue
#         else:
#             print('Row #' + str(reader.line_num) + ' ' + str(row))
    
'''
ADDS LIST TO NEW ROW IN DOCUMENT
'''
# fields=['first','second','third']
# with open(source_dir+r'\git\test-1-copy.csv', 'a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(fields)

'''
FUNCTION FOR ADDING LIST TO DOCUMENT
'''
from csv import writer

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

'''
FUNCTION FOR ADDING DICTIONARY TO DOCUMENT
'''
from csv import DictWriter

def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)
        
'''
EXTRACTS A DICTIONARY OF A SPECIFIED COLUMN
'''
# with open(source_dir+file_name, 'r', newline='') as read_obj:
#     DictReader = csv.DictReader(read_obj)
#     for row in DictReader:
#         print(row)
#         date_col = {'Date': []}
#         for record in DictReader:
#             date_col['Date'].append(record['Date'])

'''
THIS WRITES TO DOCS BUT OVERWRITES EXISTING CONTENT
'''    
# Writer Objects
# outputFile = open(source_dir+r'\git\test-1-cp.tsv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['cherries', 12, 8, '15%'])
# outputWriter.writerow(['grapes', 8, 6, '10%'])
# outputWriter.writerow(['lemons', 4, 1])
# outputFile.close()

'''
COLLECTS DICTIONARIES TO A LIST WITH SPECIFIED KEY VALUES
'''

# list = []
# def collect_dicts():

#     with open(source_dir+file_name, 'r', newline='') as read_obj:
#         DictReader = csv.DictReader(read_obj)
#         for row in DictReader:
#             if row['specified-key'] != 'specified-value' and row not in list:
#                 list.append(row)





