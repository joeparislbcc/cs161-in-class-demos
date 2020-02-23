#! /usr/bin/env python3.7

import csv

with open("users.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(f'{row["id"]} {row["last_name"]} {row["first_name"]} {row["email"]}')
