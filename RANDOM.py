import random
activities_to_do = ['a','b','c']
going_to_do = activities_to_do[2]
print "We can do " + str(activities_to_do)
print "We will do " + going_to_do


import random, urllib2
activities_to_do = urllib2.urlopen('https://raw.githubusercontent.com/bellcodo/potential-octo-chainsaw/master/code_activities_we_like.lst').read()
stuff = activities_to_do.split()
going_to_do = random.choice(stuff)
print "We can do " + str(stuff)
print "We will do " + going_to_do
import random, urllib2
activities_to_do = urllib2.urlopen('https://raw.githubusercontent.com/bellcodo/potential-octo-chainsaw/master/code_activities_we_like.lst').read()
stuff = activities_to_do.split()
going_to_do = random.choice(stuff)
print "We can do " + str(stuff)
print "We will do " + going_to_do
