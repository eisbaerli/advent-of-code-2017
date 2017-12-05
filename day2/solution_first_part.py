#!/usr/bin/python

#Open the input file
file = open("input", "r");
sheet = [map (int, line.split("\t")) for line in file]
print "Got this input = ", sheet

checksum = 0;
for line in sheet:
	mininmum = min(line);
	maximum = max(line);
	difference = maximum - mininmum;
	checksum += difference;

print "Result", checksum
#Close the input file
file.close();

