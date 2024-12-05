# Advent of Code 2024
# Day 1, Part 2
# December 4, 2024

import numpy as np

total_score = 0

# read in the file
input_file = np.loadtxt('day1-input.dat', dtype=int)

# split the data into two arrays
array1 = input_file[:, 0]
array2 = input_file[:, 1]

# sort the arrays
sorted_array1 = np.sort(array1)
sorted_array2 = np.sort(array2)

# loop through the first array
for i in range(len(sorted_array1)):

   # find the number of occurences of the current value in the second array
   occurrences = np.count_nonzero(sorted_array2 == sorted_array1[i])

   if occurrences > 0:

      # calculate the simularity score
      score = (sorted_array1[i] * occurrences)
      print('Row', i, ':', sorted_array1[i], 'occurs', occurrences, 'times, score =', score)

      # keep a running total
      total_score += score

print('\n*** The total simularity score is:', total_score, ' ***')
