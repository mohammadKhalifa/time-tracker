#!/bin/bash

import os
import sys
import utility
import time

THRD_PARTY_DIR = './/3rd_party//'

sys.path.append(THRD_PARTY_DIR)


def get_active_window_now():
    s = os.system(THRD_PARTY_DIR + "get_active.sh > shell_output_temp.txt");
    f= open('shell_output_temp.txt' , 'r')
    s = str(f.read()).strip()
    return s[s.find('\"')+1:-1]

def write_dict_to_file(data_dict , filename) :
    f = open (filename , 'w+')
    f.seek(0)
    f.truncate() #delete old content
    
    for app , t in data_dict.items():
        f.write(app+';'+t+'\n')
    
    f.close()
    
def track_and_record(file_name = "data.dat" , delay_in_mins = 3): 
    
    file_dict = record_file_to_dict(file_name)
    
    while True :
        active_app = get_active_window_now()
        file_dict.setdefault(active_app , "00:00")
        file_dict[active_app] = utility.add_time(file_dict[active_app] ,"00:"+ str(delay_in_mins))
        write_dict_to_file(file_dict , file_name)
        time.sleep(delay_in_mins * 60);


def record_file_to_dict(file_name) :
    ret_dict = {}
    f = open(file_name , 'w+')
    for line in f.readlines():
        app , time = line.split(';')
        ret_dict[app] = time.strip()
    f.close()
    return ret_dict

  
def main():
    
    if sys.argv[1] == "--start" :
        track_and_record(delay_in_mins=1);
    elif sys.argv[1] == "--stats" :
        print_stats();
    else :
        print "unknown command\n"

    


main()

