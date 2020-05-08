# Dictionaries are such data structures that can store (key,value) pairs
# initialize
my_dict = {}

# add items
my_dict['name'] = 'brian'
my_dict['state'] = 'florida'
my_dict['age'] = 37

print my_dict

# access elements
print my_dict['age']

# change elements
my_dict['name'] = 'Mate Budai'
print my_dict

# remove element by index
del my_dict['state']
print my_dict

# iterate
for k, v in my_dict.iteritems():
	print k, '=>', v
