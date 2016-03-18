import json

from pandas import read_excel
from tqdm import tqdm

def extract(data_file):
    """ Get the data! """
    desc = open(data_file, 'r')
    df = read_excel(data_file)
    desc.close()

    # [{'name': 'foo', 'fare': 1.00}, ..]
    return [entry.to_dict() for idx, entry in tqdm(df.iterrows(), leave=True)]


def transform(data):
    """ Manipulate the data! """

    def contrived_work(row):
        work = 0
        while work < 500000:
            work += 1

        return row

    return contrived_work(data)

def load(data):
    """ Store the data! """
    with open('output/titanic.json', 'w') as desc:
        desc.write(json.dumps(data, indent=4))


def run():
    #########
    # Extract
    #########
    data = extract('data/titanic3.xls')

    #########
    # Transform
    #########
    # work on one row at a time:
    modified_data = []
    for row in tqdm(data, leave=True):
        modified_data.append(transform(row))

    #########
    # Load
    #########
    load(modified_data)

