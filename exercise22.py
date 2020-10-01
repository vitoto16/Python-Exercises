"""
Given a .txt file that has a list of a bunch of names, count how many of each name there
are in the file, and print out the results to the screen. I have a .txt file for you, if
you want to use it!

Extra:

Instead of using the .txt file from above (if you want the challenge), take this .txt file,
and count how many of each “category” of each image there are. This text file is actually
a list of files corresponding to the SUN database scene recognition database, and lists
the file directory hierarchy for the images. Once you take a look at the first line or two
of the file, it will be clear which part represents the scene category. To do this, you’re
going to have to remember a bit about string parsing in Python 3.
"""

import re

pattern = re.compile(r'/[a-zA-Z]{3,}/[a-zA-Z]+/')

category_dict = dict()

with open('exercise22.txt', 'r') as f:
    file_content = f.read()

matches = pattern.findall(file_content)

for match in matches:
    match = match.strip('/')
    if match not in category_dict:
        category_dict[match] = 1
    else:
        category_dict[match] += 1

for key, value in category_dict.items():
    print(f"The '{key}' category has {value} pictures!")
