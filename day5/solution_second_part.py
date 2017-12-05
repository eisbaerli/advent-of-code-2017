#!/usr/bin/python

#Open the input file
file = open("input", "r");
numbers = [line.rstrip('\n') for line in file]
list = [int(d) for d in numbers]
#list = [0,3,0,1,-3];
print "Got this input = ", list

steps = 0;
current_position = 0;
while current_position >= 0 and current_position < len(list):
	jump_offset = list[current_position];
	if jump_offset >= 3:
		list[current_position] -= 1;
	else:
		list[current_position] += 1;
	current_position += jump_offset;
	steps += 1;
	#print "Status: ", list, " jump_offset = ", jump_offset, " position = ", current_position 


print "Produced this output = ", list

print "Result", steps
#Close the input file
file.close();

