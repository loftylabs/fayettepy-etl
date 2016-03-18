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

    def pclass_human(classnum):
        classmap = {
            1: "First",
            2: "Second",
            3: "Third",
        }
        return classmap.get(classnum, 'Unknown')

    for row in tqdm(data, leave=True):
        row['pclass'] = pclass_human(row['pclass'])

    return data

def load(data):
    """ Store the data! """
    with open('output/titanic.json', 'w') as desc:
        desc.write(json.dumps(data, indent=4))


def run():
    data = extract('data/titanic3.xls')
    modified_data = transform(data)
    load(modified_data)

