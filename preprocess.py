import numpy as np
import glob
from tqdm import tqdm

def preprocess(file_name):
    with open(file_name, "r") as r, open(file_name[:-4] + "_.csv", "w") as w:
        for line in r:
            values = line.split(',')
            w.write("{},{},{}\n".format(values[5], values[11], values[10]))

files = glob.glob("./trip_data/*.csv")

for f in tqdm(files):
    preprocess(f)
