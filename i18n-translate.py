import json
import goslate
import sys

original_data = {}

with open(sys.argv[1], 'r') as f:
    original_data = json.load(f)

print original_data
