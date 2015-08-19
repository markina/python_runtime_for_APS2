import json
from ordereddict import OrderedDict
import pprint

d = '{"aa":1, "c":{"qq":1, "q1":11, "aa2":2}, "ab":11}' 

#def mygetattr(self, name):
#    self.__getattr__(name)
#    print "in mygetattr!!"
#    print name
#    return "name" + name
    #return self.__dict__[name]

#def myinit(self, s, **kw):
#    print "init!!"

#OrderedDict.__init__ = myinit
#OrderedDict.__getattr__ = mygetattr

my_ordered_dict = json.loads(d, object_hook=OrderedDict)
print my_ordered_dict

print json.dumps(my_ordered_dict, indent=8)

print my_ordered_dict['aa']
print my_ordered_dict['aa']
print my_ordered_dict['c']
