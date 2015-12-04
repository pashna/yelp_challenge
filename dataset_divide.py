#!/usr/bin/python

import csv
import random

PART_VAL = 1/10.;

BASE_PATH    = "dataset/"
DIVIDE_FILES = ["businesses.csv", "checkins.csv", "reviews.csv", "tips.csv", "users.csv"]

for f_name in DIVIDE_FILES:
    f_path = BASE_PATH + f_name
    f_in   = open(f_path, 'rU') # 'U' for universal-newline mode
    f_out  = open(BASE_PATH + "part_" + f_name,'w')
    random.seed(42) # For repeatability
    csv_in  = csv.reader(f_in,  delimiter=',')
    csv_out = csv.writer(f_out, delimiter=',')
    is_title = True
    for row in csv_in:
        if is_title:
            csv_out.writerow(row)
            is_title = False
        else:
            if random.random() <= PART_VAL:
                csv_out.writerow(row)
    
