#! /usr/bin/python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))

# class Person(object):
#     pass
age = 25
height = "6'2\""

floatDivision = 8 / 5 # division returns floating point variable
floorDivision = 8 // 5
squared = 5**2
powers = 5**3

print("Age:",age) # seperate line
print("Height:",height) # ... prints
print(
"Float Division:",floatDivision,
"| Floor Division:",floorDivision,
"| Squared:", squared,
"| Powers:", powers) # single line print
