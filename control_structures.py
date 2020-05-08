# if/else/elif
# YOU MUST END EXPRESSION WITH A ':'
age = 17

if age >= 18:
	print 'is an adult'
elif age >= 12:
	print 'teenager'
elif age >= 3:
	print 'child'
else:
	print 'baby'

# ternary - variables have no scope?!
if age >= 21:
	old_enough = True
else:
	old_enough = False

old_enough = True if age >= 21 else False

print old_enough

while age < 50:
	print 'not old enough, current age is %d' % age
	age += 1
