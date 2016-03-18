import multiprocessing
from tqdm import tqdm

from pipeline_atomic import extract, transform, load

modified_data = []

def do_transform(row):
    """
    Executed in a subprocess, this function calls transform() and stores the result in memory
    """
    modified_data.append(transform(row))

def run():
    #########
    # Extract
    #########
    data = extract('data/titanic3.xls')

    #########
    # Transform
    #########
    # work on many rows simultaneously

    for row in tqdm(data, leave=True):
        p = multiprocessing.Process(target=do_transform, args=(row,))
        p.start()

    #########
    # Load
    #########
    load(modified_data)

