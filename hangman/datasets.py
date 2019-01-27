import json
import os

dataPath = 'data'
def getData():
    data = []
    for path in os.listdir(dataPath):
        group = {'category':path.split('.')[0]}
        with open(os.path.join(dataPath,path)) as f:
            group['words'] = json.load(f)
        data.append(group)
    return data
getData()