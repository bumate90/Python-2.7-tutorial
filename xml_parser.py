# more info on this subject on:
# https://docs.python.org/2/library/xml.etree.elementtree.html

import os
from xml.etree import ElementTree


# a simple function for updating a course
# inputs: dom tree, registration number, new title


def updateCourseTitle(dom, reg_num, new_title):
    items = dom.findall('course')
    for e in items:
        num = int(e.find('reg_num').text)
        if reg_num == num:
            node = e.find('title')
            node.text = new_title


file_name = 'read_college_courses.xml'
# to figure absolute path if it's needed
full_path = os.path.abspath(os.path.join('', file_name))
print(full_path)

# parse xml file -> output dom
dom = ElementTree.parse(full_path)
print(dom)

# needs xpath expression!!!
# example 1: finding all courses
courses = dom.findall('course/title')

for c in courses:
    print(c.text)


# example 2: finding course related info
print '**************************************'
courses2 = dom.findall('course')

for c in courses2:

    title = c.find('title').text
    num = c.find('crse').text
    days = c.find('days').text

    print(' * {} [{}] {} '. format(
        num, days, title
    ))

# example 3: changing one xml node value
print '**************************************'
for c in courses2:

    reg_num = int(c.find('reg_num').text)
    if 10486 == reg_num:
        title = c.find('title')
        print 'item found: %s' % title.text
        title.text = 'REKT!!!'
        # to highlight updated fields
        # title.set('updated', 'yes')

updateCourseTitle(dom, 10180, 'bumatepwnz')
dom.write('test_output.xml')
