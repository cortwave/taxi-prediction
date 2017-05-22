import glob
import pandas as pd
from joblib import Parallel, delayed
from tqdm import tqdm

def group(file_name):
    df = pd.read_csv(file_name, header=None)
    if len(df) > 3000:
        times = df[0].apply(lambda x: pd.to_datetime(x))
        times.index = times
        s = times.groupby(pd.TimeGrouper('1h')).count()
        s.to_csv("./grouped_by_time/{}.csv".format(hash(file_name)), header=None)

files = glob.glob("./grouped_by_zone/*.csv")

Parallel(n_jobs=-1)(delayed(group)(f) for f in tqdm(files))
    
