import os
import json

from pprint import pprint

with open('createUiDefinition.json') as cuif:
    createUi = json.load(cuif)

with open('mainTemplate.json') as mtf:
    mt = json.load(mtf)

print(json.dumps(createUi['parameters']['outputs'], indent=4))
#print(json.dumps(mt['parameters'], indent=4))

for icu in createUi['parameters']['outputs']:
    found=False
    for imt in mt['parameters']:
        if icu == imt:
           found=True
    if found == False:
        print('Not found: ' + icu)
