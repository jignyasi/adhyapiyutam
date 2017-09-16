import time

#Method-1
def fnSquare(x):
    time.sleep(0.1)
    y = pow(x, 2)
    return y

def fnCube(x):
    time.sleep(0.2)
    y = pow(x, 3)
    return y

print fnSquare(2), fnCube(3)

#Measure time for exec in each func
x = 2
t1 = time.time()
print "Input for fnSquare is {0}".format(x)
fnSquare(2)
print "Total exec time for fnSquare is {0}".format((time.time()-t1)/60)

x = 3
t1 = time.time()
print "Input for fnCube is {0}".format(x)
fnCube(3)
print "Total exec time for fnCube is {0}".format((time.time()-t1)/60)


#Method-2
def fnSquare(x):
    print "\nInput for fnSquare is {0}".format(x)
    time.sleep(0.1)
    y = pow(x, 2)
    print "\nTotal exec time for fnSquare is {0}".format((time.time()-t1)/60)
    return y

def fnCube(x):
    print "\nInput for fnCube is {0}".format(x)
    time.sleep(0.2)
    y = pow(x, 3)
    print "\nTotal exec time for fnCube is {0}".format((time.time()-t1)/60)
    return y

print fnSquare(2), fnCube(3)


#Method-3 : Wrapper
def WRAPPERFUNC(func,*args, **kwargs):
    t1 = time.time()    
    func(*args, **kwargs)
    print "\nTotal exec time is {0}".format((time.time()-t1)/60)
    return None

def f1():
    print "this is f1 return 10"
    return None

print f1()
print WRAPPERFUNC(f1)
print WRAPPERFUNC(f2)

#Method-4 : Decorator 
def myWrapper(func):
    def coreWrapper(*args, **kwargs):
        print "\nInput is {0}".format(x)
        t1 = time.time()
        z = func(*args, **kwargs)
        print "\nTotal exec time is {0}".format((time.time()-t1)/60)
        return z
    return coreWrapper

@myWrapper
def fnSquare(x):
    time.sleep(0.1)
    y = pow(x, 2)
    return y

@myWrapper
def fnCube(x):
    time.sleep(0.2)
    y = pow(x, 3)
    return y

print fnCube(3), fnSquare(2)


#Class
#Company--Permanent employees, temporory
class LIC:
    def fnHello(self):
        print "Hello LIC Employee!"

lic = LIC()
lic.fnHello()

class LIC:
    def __init__(self, eName, eAge):
        self.eName = eName
        self.eAge = eAge

lic = LIC('Rama', 55)
print lic.eName

class LIC:
    def __init__(self, eName, eAge):
        self.eName = eName
        self.eAge = eAge

    def fnHello(self):
        print "Hello LIC Employee {0}!".format(self.eName)

lic = LIC('Rama', 55)
print lic.eName
lic.fnHello()

class LIC:
    def __init__(self, eName, eAge):
        self.eName = eName
        self.eAge = eAge

    def fnHello(self):
        print "Hello LIC Employee {0}!".format(self.eName)

    def fnFullInfo(self):
        self.fnHello()
        print "Your age is {0}".format(self.eAge)

lic = LIC('Rama', 55)
lic.fnFullInfo()

class LIC:
    def __init__(self, eName, eAge):
        self.eName = eName
        self.eAge = eAge

    def fnHello(self):
        print "Hello LIC Employee {0}!".format(self.eName)

    def fnFullInfo(self):
        self.fnHello()
        print "Your age is {0}".format(self.eAge)

    def fnDesg(self, desg):
        print "Hello LIC Employee {0}!, your age is {1} and \
        your designation is {2}".format(self.eName, self.eAge, desg)

lic = LIC('Rama', 55)
lic.fnDesg('CASHIER')

class LIC:
    def __init__(self, eName, eAge):
        self.eName = eName
        self.eAge = eAge

    def fnHello(self):
        print "Hello LIC Employee {0}!".format(self.eName)

    def fnFullInfo(self):
        self.fnHello()
        print "Your age is {0}".format(self.eAge)

    def fnDesg(self, desg):
        self.desg = desg
        print "Hello LIC Employee {0}!, your age is {1} and \
        your designation is {2}".format(self.eName, self.eAge, desg)

    def fnNextPost(self):
        if self.desg == 'CASHIER':
            print 'your next post is {0}'.format('HGA')
        elif self.desg == 'HGA':
            print 'your next post is {0}'.format('AAO')

lic = LIC('Rama', 55)
lic.fnDesg('CASHIER')
print lic.desg
print lic.fnNextPost()

lic = LIC('Rama2', 55)
print lic.fnNextPost()

class LIC:
    def __init__(self, eName, eAge):
        self.eName = eName
        self.eAge = eAge
        self.MYCONST = 3.3
    
    @staticmethod    
    def fnHello1():
        print "Hello LIC Employee!"

    @staticmethod
    def fnHello2(name):
        print "Hello Employee your name is {0}!".format(name)

    def fnFullInfo(self):
        #self.fnHello()
        print "Your age is {0}".format(self.eAge)

    def fnDesg1(self):
        print "Hello LIC Employee {0}!, your age is {1} \
        ".format(self.eName, self.eAge)

    def fnDesg(self, desg):
        self.desg = desg
        print "Hello LIC Employee {0}!, your age is {1} and \
        your designation is {2}".format(self.eName, self.eAge, desg)
        
    def fnNextPost(self):
        if self.desg == 'CASHIER':
            print 'your next post is {0}'.format('HGA')
        elif self.desg == 'HGA':
            print 'your next post is {0}'.format('AAO')

print LIC.fnHello1()
print LIC.fnHello2('VAMSEE')

class EMPLOYEE(LIC):
    def __init__(self, eName, eAge, eSalary):
        LIC.__init__(self, eName, eAge)
        self.eSalary = eSalary

    def fnSalPrint(self):
        self.fnDesg1()
        print 'Your salary is {0}'.format(self.eSalary)

emp = EMPLOYEE('Mouni',25,'9L')
print emp.eName, emp.MYCONST
emp.fnSalPrint()