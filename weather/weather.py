import xmltodict
import argparse
import json
import os
parser = argparse.ArgumentParser()
parser.add_argument('filePath')

filePath = parser.parse_args().filePath
fileName = os.path.splitext(filePath)[0]
with open(filePath) as fXml:
    doc = xmltodict.parse(fXml.read())
with open(fileName + '.json','w') as fJson:
    
    json.dump(doc, fJson,indent='\t')
    # print(doc)