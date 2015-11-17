"""
The purpose of this program is to perform an insertion sort.

This program will first generate a list of 100 random numbers
between 0 and 200.  This list will be sorted by the insertion 
sort function

The program iterates over each position in the integer array,
comparing each value to the positions before them and inserting
the value into the proper position in a least to greatest order

"""
import random

class InsertSort():

	def __init__(self):

		#Instantiate the random list
		ints = self.irand(100, 200)

		#Print the unsorted list
		print("\n")
		print("Unsorted list: " + "\n")
		print(ints)
		print("\n")
		
		#Print the sorted list
		print("Sorted list: " + "\n")
		print(self.insSort(ints))	

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

	#The irand function from project 5
	def irand(self, n, m):
		b = list(range(n))
		b = random.sample(range(m), n)
		return b

I = InsertSort()