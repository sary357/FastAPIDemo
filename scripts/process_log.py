import sys
from datetime import date
import os, shutil
import json

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
                if "save_vote" in line and "Process" in line and "MainThread" in line and "CRITICAL" in line:
                    timestamp=line.split(': ')[0]
                    user_input=line.split("save_vote")[1].split("MainThread")[1].split(')):')[1].strip()
                    user_input_json=json.loads(user_input)
                    user_input_json['log_time']=timestamp
                    out.write(str(user_input_json)+"\n")

if __name__ == "__main__":
    log_file_path = sys.argv[1]
    out_file_path = sys.argv[2]
    print(f"Start to generate. Output file path: {out_file_path}")
    process_log(log_file_path, out_file_path)
    print(f"Generate the output file successfully: {out_file_path}")