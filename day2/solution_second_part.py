#!/usr/bin/python

#Open the input file
file = open("input", "r");
sheet = [map (int, line.split("\t")) for line in file]

#sheet = [[5,9,2,8], [9,4,7,3], [3,8,6,5]]
print "Got this input = ", sheet

checksum = 0;
for line in sheet:
	for a in line:
		for b in line:
			if a%b == 0 and a != b:
				checksum += a/b;

print "Result", checksum
#Close the input file
file.close();

