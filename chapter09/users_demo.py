#! /usr/bin/env python3.7

import csv

with open("users.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    row_count = 0
    for row in csv_reader:
        if row_count == 0:
            print(f'Field names are: {", ".join(row)}')
        else:
            print(f"id: {row[0]} last name: {row[1]} first name: {row[2]} email address: {row[3]}")
        row_count += 1
print(f"Processed {row_count} lines")
