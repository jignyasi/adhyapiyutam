# import os, sys
# sys.path.insert(0, '/usr/local/lib/python2.7/site-packages') ##***
# import re,requests
# import bs4 as bs
# resp = requests.get('https://python.swaroopch.com/?q=#frontpage')
# soup = bs.BeautifulSoup(resp.text, 'lxml')
# contents = soup.findAll('a',{'href':re.compile(".*html")})
# for content in contents[5:16]:
#     print re.sub('\n            ','',content.text).strip()

print 'hello'

a = 'hello'

if(a == b){
    do this
}

if a==a:
    print '1'
    print '2'
print 'something'

if True:
    print '1'
    if True:
        print '2'
        if "True":
            print '3'

name = 'anand'
age = 28
loc = 'hyd'
print 'hi, my name is {0} and my age is {1} and my loc is {2} and my sal is {1}L'.format(name,age,loc)

print float(2) / 3
print 17 // 3 
print 17 % 3 
print 2 ** 6
print pow(2,5)

print not (True and True)
print not (True or False)
print not (True | False)
print not (True & True)
print 3!=3

a = 3
a+=1
print a
a*=2
print a

if a<10:
    print 'level-0 {0}'.format(a)
elif a < 20:
    print 'level-1 {0}'.format(a)
else:
    print 'level-2 {0}'.format(a)

flag = 0
while flag <5:
    print flag
    flag+=1

for flag in range(5):
    print 'something'
    if flag ==2:
        continue
    print flag
    if flag == 4:
        break

def myfun():
    print 'hello world!'
    return None

myfun()

def myfun(x):
    return 'hello world!{0}'.format(x)

print myfun()
print myfun('BISCUIT')


def myfun(x = 'BAZINGA'):
    return 'hello world!{0}'.format(x)

print myfun()
print myfun('BISCUIT')

# Local variable scope
x = 10
def myfun(y):
    x =2*y
    return 'hello world!{0}'.format(x)
print myfun(x)
print(x)

# global variable scope
x = 40
def myfun(y):
    global x
    x =2*y
    return 'hello world!{0}'.format(x)
print myfun(x)
print(x)

# kwargs example -- numbers
def myfun(*numbers):
    print numbers
    return sum(numbers)

print myfun(2,3,4,5,6, 6.3)


def myfun(**vars):
    print vars
    return vars['x'] + vars['y']

print myfun(x = 2, y = 10, z = 100, h = 200)

def myfun(x,y, *nums, **kwargs):
    print x,y
    print nums, kwargs
    return x+y+kwargs['z'] + sum(nums)

print myfun(2,4,6,8,z = 100, h = 200)


#sys.path.insert(fileWD)
import sampleProg1
sampleProg1.fnCopy('choc', 'biscuit')


from sampleProg1 import fnCopy1, fnCopy2
fnCopy1('choc', 'biscuit')

from sampleProg1 import *
fnCopy2('choc', 'biscuit')


import sampleProg1
dir(sampleProg1)

from myPackage1 import sampleProg1
sampleProg1.fnCopy1('source1', 'destination1')


x = 2
print type(x)
x = 2.2
print type(x)
x = '2.2'
print type(x)
x = 'abcdefghijklmno'
print type(x)
print x[0:3]
print x[:-1]
print x[::-1]
print x[::2]
print dir(x)
print len(x)
print x.isupper()
print x.upper()
print x.replace('k','K')
print x + '123'

x = ['a',2, 'b',3 ,'c']
print type(x)
print len(x)
print x[0:3]
print x[-1]
print x[:-1]
print x[::2]
print x + list('xyz')
print x + ['1','2','22','33']
print dir(x)
x.sort()
print(x)
x.append('yellow')
print(x)
x.append(['blue', 'red'])
print(x)
x.extend(['pink', 'green'])
print(x)
x.insert(2, 'MENTAL')
print x
x.reverse()
print x
x.pop(3)
print x
x.remove('a')
print x
y = x.pop(1)
print x,y
print sum([0,1,2])
print sum([True, False, True])

x = ['a','a','b','b','b','c']
y = ['b','c','c','c','d']
print set(x) - set(y)
print set(x).union(set(y))
print set(x).intersection(set(y))
print list(set(x).union(set(y)))

x = ['a',2, 'b',3 ,'c']
#M1
y = []
for k in x:
    y.append(str(k)+'L')
print y

#M2
y = [str(k)+'L' for k in x]

#M3
y = map(lambda k: str(k)+'L',x)

#########
filter(lambda k: k>5, range(10))
reduce(lambda a,b: a+b, range(10))
k = []
reduce(lambda a,b: k.append([a,b]), [22,1,2,44,7,3,8])
print k

####Vectorized operations
y = ['1','2','22','33']
x = '_'.join(y)
print x
print x.split('_')

y = ['1',2,'22',33,'abc']
print '+'.join(map(str, y))

print [2,3] #this is a list
print (2,3) #this is a tuple
k = [2,3]
k.append(4)
print k

x = (2,3,4,5,6,7) #immutable
print type(x)
print len(x)
print x[0:3]
print dir(x)
#print x.count(4)
print x.index(4)
x = [('username','password1'),('username1','password2')]
print x
print map(lambda k: 
    '+'.join(k),
    x)

def myJoinfunc(l):
    return '+'.join(l)

print map(myJoinfunc, x)    

print (('username','password1'),('username1','password2'))

a,b = 2,3
print a,b
a,b,_ = 2,3,4
print a,b
a,b = ('AB','CD')
print a,b

x = [('username','password1'),('username1','password2')]

def myJoinfunc(l):
    a,b = l
    return '+'+a+'::'+b
print map(myJoinfunc, x)

x = (('username','password1'),('username1','password2'))
print map(myJoinfunc, x)
print (2,3) # length 2
print (2) #will not be a tuple
print (2,) # length 1

[]#Search is index based
()#Search is index based
{}#Search is key based
x = {'username':'password','username1':'password1','username2':'password2'}
print type(x)
print len(x)
print x['username1']
print x.keys()
print x.values()
for k in x:
    print [k,x[k]]
print [[k,x[k]] for k in x]
x['username3'] = 'password3' #adding a new user
print x
print dir(x)
for usr,pasw in x.items():
    print usr+pasw
x.pop('username3')
print x
del x['username2']
print x
print x['username1']
x['username1'] = 'MYPASSWORD'
print x['username1']

x = {'username':['password',22,'M','HYD'],
'username1':'password1',
'username2':('password2','M'),
'username3': {'LOC':'HYD','Age':28,'PASSWORD':'abcxyz'}}
print x
print x['username']
print x['username'][3]
print x['username3']
print x['username3']['LOC']

a = list('abcde')
b = a
a.remove('c')
print a,b
a = list('abcde')
b = a[:] ##Copy
a.remove('c')
print a,b
a = zip(list('abcde'),list('fghij'))
a = dict(a)
b = a
a.pop('c')
print a,b
a = zip(list('abcde'),list('fghij'))
a = dict(a)
b = a.copy()
a.pop('c')
print a,b


import re
rex = re.compile('\(.*?\)')
A = 'acf () (hihhh) (ashd|} dashfj'
print re.sub(rex, '', A)
rex = re.compile('\(.*?\)|\[.*?\]')
A = 'acf () (hihhh) (ashd|} dashfj p[ascsf]'
print re.sub(rex, '', A)
rex = re.compile('\(.*?\)|\[.*?\]')
rex = re.compile('\(\w+?\)')
print re.sub(rex, '', A)