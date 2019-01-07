import sys
import json

target = sys.argv[1]

with open(target) as json_data:
    
    data = json.load(json_data)

    data['extensions'].pop('VRM')
    data['extensionsUsed'].remove('VRM')

    with open(target, 'w') as outfile:
        json.dump(data, outfile)