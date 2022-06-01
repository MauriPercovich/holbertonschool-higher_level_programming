#!/usr/bin/python3
'''module add_item'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    _list = load_from_json_file(filename)
except FileNotFoundError:
    file = []
for i in sys.argv[1:]:
    file.append(i)
save_to_json_file(file, "add_item.json")
