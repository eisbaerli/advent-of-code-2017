#!/usr/bin/python
import math

input = 361527;

print "Got this input: ", input;

sqrt = math.sqrt(input);
ceil = math.ceil(sqrt) * math.ceil(sqrt);
floor = math.floor(sqrt) * math.floor(sqrt);

sqrt_floor = math.sqrt(floor);
sqrt_ceil = math.sqrt(ceil);


difference = ceil - floor - 1
half = floor + difference / 2;

difference_input_floor = input - floor;
difference_ceil_input = ceil - input;

input_coordinates = 0;

isLowerLeft = ceil%2 == 1;
if isLowerLeft:
	if input <= half:
		input_coordinates = [ - sqrt_floor/2, sqrt_floor/2 - difference_input_floor + 1];
	else:	
		input_coordinates = [math.floor(sqrt_ceil/2) - difference_ceil_input, - math.floor(sqrt_ceil/2)];
else:
	if input <= half:
		input_coordinates = [math.floor(sqrt_floor/2), -math.floor(sqrt_floor/2) + difference_input_floor];
	else:
		input_coordinates = [ - math.floor(sqrt_ceil/2) + difference_ceil_input + 1, math.floor(sqrt_ceil/2)];

manhatten_distance = abs(input_coordinates[0]) + abs(input_coordinates[1])

print "Input coordintes = ", input_coordinates;
print "Manhatten Distance = ", manhatten_distance;
