#!/usr/bin/python

#Open the input file
file = open("input", "r");
number = int(file.read());

print "Got this input = ", number
digits = [int(d) for d in str(number)]

position = len(digits)/2;
halfway = digits[position];

sum = 0;
for index, digit in enumerate(digits):
	if digit == halfway:
		sum += digit;
	halfway = digits[(position+index+1)%len(digits)];

print "Result = ", sum

#Close the input file
file.close();

