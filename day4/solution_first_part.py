#!/usr/bin/python

#Open the input file
file = open("input", "r");
passphrases = [line.rstrip('\n') for line in file]
passphrases = [map (str, line.split(" ")) for line in passphrases]
print "Got this input = ", passphrases

valid = 0
for line in passphrases:
	found_duplicates = 0;
	for i, word in enumerate(line):
		for j, other in enumerate(line):
			if word == other and i != j:
				found_duplicates += 1;
	if found_duplicates == 0:
		valid += 1;

print "Result = ", valid

#Close the input file
file.close();

