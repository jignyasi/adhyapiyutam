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
