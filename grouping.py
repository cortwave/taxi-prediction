from tqdm import tqdm
from joblib import Parallel, delayed
import glob

def group(file_name):
    print("starting group {} file".format(file_name))
    with open(file_name, "r") as r:
        r.readline()
        for line in r:
            values = line.split(",")
            write_file = "./grouped_by_zone/" + str(int(float(values[1]) / 0.01)) +  ":" + str(int(float(values[2]) / 0.01)) + ".csv"
            with open(write_file, "a") as w:
                w.write("{}\n".format(values[0]))
    print("finished group {} file".format(file_name))

files = glob.glob("./trip_data/*.csv")

Parallel(n_jobs=-1)(delayed(group)(file_name) for file_name in files)
