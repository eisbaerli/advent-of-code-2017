#!/usr/bin/python

#Open the input file
file = open("input", "r");
number = int(file.read());
print "Got this input = ", number
digits = [int(d) for d in str(number)]

previous = digits[-1];
sum = 0;
for index, digit in enumerate(digits):
	if digit == previous:
		sum += digit;
	previous = digit;

print "Result = ", sum

#Close the input file
file.close();

