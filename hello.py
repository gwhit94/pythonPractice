#! /usr/bin/python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))

# class Person(object):
#     pass
boot = "boot"
age = 25
height = "6'2\""

floatDivision = 8 / 5 # division returns floating point variable
floorDivision = 8 // 5 # divison returns int
remainder = 8 % 5
divMod = divmod(8,5) # the pair (x // y, x % y)

squared = 5 ** 2 # = pow(5,2)
powers = 5 ** 3 # = pow(5,3)
mixed = 5 * 3.2 - 8 # mixed type operands convert to floating point

absolute = abs(-5) # absolute number

print("Age:",age)       # seperate line
print("Height:",height) # ... prints
print(
"Float Division(8/5):",floatDivision,
"| Floor Division(8//5):",floorDivision,
"| Remainder(8%5):", remainder,
"| divmod(8,5):", divMod)
print(
"Squared(5**2):", squared,
"| Powers(5**3):", powers,
"| Mixed Operands(5**3.2 - 8):", mixed) # single line print

print("Absolute(-5):",absolute)
print("\nSeperate \nLines")# seperate lines in same print
print("""\n\
Multi line:
    String
    Literals!
""")# Multi line string literals

print(8 * "unce" + " BASS", "Auto" "matic") # repeated string then concat / Automatic concat
print(boot[1] * 2 + boot[-4]) # index ref > repeat > concat > index from right
print("t" + boot[1:4], boot[:2] + "b") # slicing
print(len("montypythonsflyingcircus"))

# Fibonacci Series
# the sum of two elements defines next iteration
a, b = 0, 1
while a < 55:
    print(b)
    a, b = b, a+b
