import justpy as jp
import sqlite3
import pandas as pd
import parseData
import web

def parse_database():
    # print("START")
    base_path = "/home/user1/OU/Semester5/CS4620/FinalProject/WMs/"
    files = (base_path + "awesome/", base_path + "dwm/", base_path + "i3/",
             base_path + "qtile/", base_path + "spectrwm/", base_path + "stumpwm/",
             base_path + "xmonad/")

    parseData.pretty_log(files)
    # print("LOGGED")

    base_path = "/home/user1/OU/Semester5/CS4620/FinalProject/Django/GitStalker/"
    files = (base_path + "awesome.txt", base_path + "dwm.txt", base_path + "i3.txt",
             base_path + "qtile.txt", base_path + "spectrwm.txt", base_path + "stumpwm.txt",
             base_path + "xmonad.txt")
    
    parseData.extract_data(files)
    # print("EXTRACTED")

    return

    
print("COMPLETE")
