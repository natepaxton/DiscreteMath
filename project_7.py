"""
The purpose of this program is to perform a binary search within a 
randomly generated list of integers between 0 and 200.

The program will first generate a list of integers using the random 
generator from project 5, and will sort the list using the insert
sort from project 6.  Binary searches can only be performed on sorted
lists.

The program will return the position of the integer being searched
for if it is present, and will return a message if not found.
"""
import random

class projectSeven:

	def __init__(self):

		#Generate the random number list
		ints = self.irand(100, 200)
		print("\nThe random list:\n" + str(ints))

		#Sort the list
		ints = self.insSort(ints)
		print("\nThe sorted list:\n" + str(ints))

		#Search for the index
		c = int(input("\nEnter an integer to search for: "))
		print(self.binSearch(ints, c))

	def binSearch(self, nums, c):
		
		#Variables to represent the start and end point, control logic
		a = 0
		b = len(nums) - 1
		found = False

		#Iterate over the values if not found
		while a <= b and not found:

			#Determine the midpoint for the search
			mid = int((a + b) // 2)

			#If the number matches, found == true
			if nums[mid] == c:
				found = True

			#Increment or decrement the upper and lower bounds depending 
			#on comparison
			else:
				if c < nums[mid]:
					b = mid - 1
				else:
					a = mid + 1

		if found:
			return "\n" + str(c) + " found at position " + str(mid + 1)

		else:
			return "\n " + str(c) + " is not in the sequence"

	def irand(self, n, m):
		b = list(range(n))
		b = random.sample(range(m), n)
		return b

	#Sort the list using an insertion sort
	def insSort(self, nums):

		#Compare the positions in the array
		for i in range(1, len(nums)):

			#The value to be compared
			currentvalue = nums[i]

			#Assign the iterator to a new variable to avoid index errors
			position = i

			#Position must be greater than zero so the index can't be -1
			while position > 0 and nums[position - 1] > currentvalue:

				#Assign the value to a new position
				nums[position] = nums[position - 1]
				position = position - 1

			#Assign the value to a new position
			nums[position] = currentvalue

		#Return the sorted array
		return nums

p = projectSeven()