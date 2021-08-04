import os
import sys
import re
import pandas as pd

if len(sys.argv)!=4:
    raise Exception('Usage: python find.py dir regex save_path')

print(f'start_dir: {sys.argv[1]}, regex: {sys.argv[2]}, save_path: {sys.argv[3]}')

start_dir=sys.argv[1]
regex=re.compile(sys.argv[2])
save_path=sys.argv[3]

all_names=[]
complete_paths=[]

for dirpath, dirnames, filenames in os.walk(start_dir):
    for f in filenames:
        if regex.match(f):
            #found a match
            all_names.append(f)
            complete_paths.append(os.path.join(dirpath,f))

out_frame=pd.DataFrame(dict(filenames=all_names,path=complete_paths))
out_frame.to_csv(save_path)
