#single line
text = "hello"
print text

#mult line
multi_line = "line1" \
	     "line2" \
	     "line3"
print multi_line

#substring syntax - start_index : end_index (end is excluded)
name = "Mate Budai"
first_name = name[0:4]
print first_name

#integer
num1 = 6
print num1

#float
dec1 = 5.4
print dec1

#conversion to string
to_string = str(num1)+"joksa"
print to_string

#coversion to integer/float
num_string = "30"
num_string2 = "30.2312"
to_int = int(num_string)
to_float = float(num_string2)
print "integer value:{0}, float value:{1}".format(to_int, to_float)

