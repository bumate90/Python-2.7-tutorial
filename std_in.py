import sys

# handling command line arguments
if len(sys.argv) < 2:
    print 'Minimum amount of command line args = 2!'
    exit()
else:
    print 'Command line arguments supplied...'

if str(sys.argv[1]) == 'Corona time':
    print 'Password accecpted!'
else:
    print 'Wrong Password!'
    exit()

# handling standard input from console
strs = ['Enter your name: ', 'Age: ', 'Address: ']

name = ''
age = -1
address = ''

for i in range(0, 3):
    s = raw_input(strs[i])
    if 0 == i:
        name = s
    elif 1 == i:
        age = int(s)
    elif 2 == i:
        address = s

if 'Mate Budai' == name and 30 == age and \
        'Sator ut 1.' == address:
    print "This is me!!!"
