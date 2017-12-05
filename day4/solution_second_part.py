#!/usr/bin/python

#Open the input file
file = open("input", "r");
passphrases = [line.rstrip('\n') for line in file]
passphrases = [map (str, line.split(" ")) for line in passphrases]
print "Got this input = ", passphrases

valid = 0
for line in passphrases:
	found_anagram = 0;
	for i, word in enumerate(line):
		letters_word = list(word);
		for j, other in enumerate(line):
			letters_other = list(other);
			if i != j and len(letters_word) == len(letters_other):
				for letter in letters_word:
					if letter in letters_other:
						letters_other.remove(letter);
			if len(letters_other) == 0:
				found_anagram += 1;
	if found_anagram == 0:
		valid += 1;

print "Result = ", valid

#Close the input file
file.close();

