#!/bin/bash

import os


def get_active_window_now():
    s = os.system(".//get_active.sh > shell_output_temp.txt");
    f= open('shell_output_temp.txt' , 'r')
    s = str(f.read()).strip()
    return s[s.find('\"')+1:-1]
    

print get_active_window_now()