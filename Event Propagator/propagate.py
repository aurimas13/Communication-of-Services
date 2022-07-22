# Python program INFINITELY

import json
import ast
import random

# # Opening JSON file
# f = open('events_propagator.json')
#
# # returns JSON object as
# # a dictionary
# data = json.load(f)
#
# # Iterating through the json
# # list
# # for i in data:
# #     print(i)
#
# # Closing file
# f.close()


with open('events_propagator.json') as f:
    data = ast.literal_eval(f.read())
    l = random.choice(data)
    print(l)
    # for i in data:
    #     # result = {k: random.choice(v) for k, v in i.items()}
    #     print(i)