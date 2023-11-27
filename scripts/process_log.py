# generate a python function that can open a file and read it line by line
# filter the lines that contain the word "b'{"

import sys
from datetime import date
import os, shutil

def process_log(log_file_path:str, out_file_path:str):
    '''
    log_file_path: the path of the log file
    out_file_path: the path of the output file
    '''
    if os.path.exists(out_file_path):
        os.remove(out_file_path)
    with open(log_file_path) as f:
        with open(out_file_path, "w+") as out:
            for line in f:
                if "b'{" in line:
                    user_input=line.split("b'")[1].split("'")[0]
                    out.write(user_input+"\n")

if __name__ == "__main__":
    log_file_path = sys.argv[1]
    out_file_path = sys.argv[2]
    process_log(log_file_path, out_file_path)