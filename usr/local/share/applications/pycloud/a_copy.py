import json
from ordereddict import OrderedDict

d = '{"aa":1, "c":{"qq":1, "q1":11, "aa2":2}, "ab":11}' 


my_ordered_dict = json.loads(d, object_hook=OrderedDict)
print my_ordered_dict

print json.dumps(my_ordered_dict)

print my_ordered_dict['aa']
#print my_ordered_dict.aa
#print my_ordered_dict.c.qq
