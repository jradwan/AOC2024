# Advent of Code 2024
# Day 1, Part 1
# December 4, 2024

import numpy as np

total_distance = 0

# read in the file
input_file = np.loadtxt('day1-input.dat', dtype=int)

# split the data into two arrays
array1 = input_file[:, 0]
array2 = input_file[:, 1]

# sort the arrays
sorted_array1 = np.sort(array1)
sorted_array2 = np.sort(array2)

# loop through the arrays
for i in range(len(sorted_array1)):

   # calculate the distance in the pairs
   distance = abs((sorted_array1[i] - sorted_array2[i]))
   print('Row', i, ':', sorted_array1[i], '-',  sorted_array2[i], '=',  distance)

   # keep a running total
   total_distance += distance

print('\n*** The total distance is:', total_distance, ' ***')
