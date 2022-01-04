import os, time, os.path
from send2trash import send2trash
    
folder = r"C:\Users\viana\Documents\infrastructure\Reports"
now = time.time()
subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]

for folder in subfolders:
  files = [f.path for f in os.scandir(folder) if f.is_file()]
  for file in files:
    if os.stat(file).st_mtime < now - 43200:
      send2trash(file)