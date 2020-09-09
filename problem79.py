'''
24/06/2020

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
'''

# While trying to think of a proper way to solve this, doing a bit of puzzling
# by hand gave the solution 73162890 in a minute or so

with open('problem79.txt') as file:
    pass
