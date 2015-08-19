import sys

# sys.path.append('/var/www/html/pycloud/')
sys.path.append('/usr/lib/python2.6/site-packages/aps2/')

from aps2.aps import ResourceBase
import aps2.uLogging


class cloud(ResourceBase):

    # def provision(self):
    
    # def unprovision(self):
    
    # def retrieve(self):
    
    # def configure(self, new):

    def __init__(self):

        self.apphost = None
        self.cloudadmin = None
        self.cloudpass = None 

    def provision(self):
        aps2.uLogging.info("IN CLOUD: new apphost = " + self.apphost)
        aps2.uLogging.info("IN CLOUD: new cloudadmin = " + self.cloudadmin)
        aps2.uLogging.info("IN CLOUD: new cloudpass = " + self.cloudpass)
        
        self.apphost = "MY_POST_apphost"
        self.cloudpass = "MY_POST_cloudpass"
        self.cloudadmin = "MY_POST_cloudadmin"  
   
    def unprovision(self):
        aps2.uLogging.info("IN CLOUD: delete")

    def retrieve(self):

        aps2.uLogging.info("IN CLOUD: old apphost = " + self.apphost)
        aps2.uLogging.info("IN CLOUD: old cloudadmin = " + self.cloudadmin)
        aps2.uLogging.info("IN CLOUD: old cloudpass = " + self.cloudpass)

        self.apphost = "MY_GET_APPHOST"
        self.cloudpass = "MY_GET_PASS"
        self.cloudadmin = "MY_GET_ADMIN" 
    
        aps2.uLogging.info("IN CLOUD: new apphost = " + self.apphost)
        aps2.uLogging.info("IN CLOUD: new cloudadmin = " + self.cloudadmin)
        aps2.uLogging.info("IN CLOUD: new cloudpass = " + self.cloudpass)

    def configure(self, new):
        
        aps2.uLogging.info("IN CLOUD: old apphost = " + self.apphost)
        aps2.uLogging.info("IN CLOUD: old cloudadmin = " + self.cloudadmin)
        aps2.uLogging.info("IN CLOUD: old cloudpass = " + self.cloudpass)
        
        aps2.uLogging.info("IN CLOUD: new apphost = " + new.apphost)
        aps2.uLogging.info("IN CLOUD: new cloudadmin = " + new.cloudadmin)
        aps2.uLogging.info("IN CLOUD: new cloudpass = " + new.cloudpass)
        
        self.apphost = "MY_PUT_apphost"
        self.cloudpass = "MY_PUT_cloudpass"
        self.cloudadmin = "MY_PUT_cloudadmin"  

    def calculateSomething(self, paramX, paramA, paramB):

        aps2.uLogging.info("IN CLOUD: paramX = %s" % paramX)
        aps2.uLogging.info("IN CLOUD: paramA = %d" % paramA)
        aps2.uLogging.info("IN CLOUD: paramB = %d" % paramB)

    def createKeyFunc(self, pathparam, OS, ps, number, querystr, bool):
        
        aps2.uLogging.info("IN CLOUD:createKeyFunc: pathparam = " + str(pathparam) + " type =" + str(type(pathparam)))
        aps2.uLogging.info("IN CLOUD:createKeyFunc: OS = " + str(OS) + " type =" + str(type(OS)))
        aps2.uLogging.info("IN CLOUD:createKeyFunc: ps = " + str(ps) + " type =" + str(type(ps)))
        aps2.uLogging.info("IN CLOUD:createKeyFunc: number = " + str(number) + " type =" + str(type(number)))
        aps2.uLogging.info("IN CLOUD:createKeyFunc: querystr = " + str(querystr) + " type =" + str(type(querystr)))
        aps2.uLogging.info("IN CLOUD:createKeyFunc: bool = " + str(bool) + " type =" + str(type(bool)))

    def createCounterFunc(self, pathparam, count):
        aps2.uLogging.info("IN CLOUD:createCounterFunc: pathparam = " + pathparam)
        aps2.uLogging.info("IN CLOUD:createCounterFunc: count = " + count)

    def testFunc(self, first, second):
        aps2.uLogging.info("IN CLOUD:testFunc: first = " + str(first) + " type = " + str(type(first)))
        aps2.uLogging.info("IN CLOUD:testFunc: second.usage = " + str(second.usage) + " type = " + str(type(second.usage)))
        aps2.uLogging.info("IN CLOUD:testFunc: second.limit = " + str(second.limit) + " type = " + str(type(second.limit)))
        
    def test_func_1(self, noti, person, name, age):
        aps2.uLogging.info("IN CLOUD:test_func_1: noti.type = " + str(noti.type) + " type = " + str(type(noti.type)))
        aps2.uLogging.info("IN CLOUD:test_func_1: noti.time = " + str(noti.time) + " type = " + str(type(noti.time)))
        
        aps2.uLogging.info("IN CLOUD:test_func_1: noti.serial = " + str(noti.serial) + " type = " + str(type(noti.serial)))
        aps2.uLogging.info("IN CLOUD:test_func_1: noti.source.type = " + str(noti.source.type) + " type = " + str(type(noti.source.type)))
        aps2.uLogging.info("IN CLOUD:test_func_1: noti.source.id = " + str(noti.source.id) + " type = " + str(type(noti.source.id)))
        
        aps2.uLogging.info("IN CLOUD:test_func_1: noti.person = " + str(person) + " type = " + str(type(person)))
        aps2.uLogging.info("IN CLOUD:test_func_1: noti.name = " + str(name) + " type = " + str(type(name)))
        aps2.uLogging.info("IN CLOUD:test_func_1: noti.age = " + str(age) + " type = " + str(type(age)))

    @staticmethod
    def test_static_func_1(name):
        
        aps2.uLogging.info("IN CLOUD: I'm static function!")
        aps2.uLogging.info("IN CLOUD: name = " + name)

