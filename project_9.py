"""
The purpose of this program is find the greatest common divisor and the
least common multiple of a list of integers.

The length of the list is arbitrary.  The greatest common divisor will be
determined using the Euclidian Algorithm.  The greatest common divisor will
then be used to determine the least common multiple.

Euclid's algorithm will be used recursively to find the GCD of the first 
two numbers, then the GCD of that number with the next number.

"""

class inCommon:

	def __init__(self):

		#Prompt the user for the number of inputs
		e = int(input("\nHow many elements are in the input?\n"))

		#Instantiate the array to hold the inputs
		nums = []

		#Enter the inputs with a for loop
		for i in range(1, e + 1):
			j = int(input("\nEnter input " + str(i) + ":\n"))
			nums.append(j)

		self.GCD(nums)

	#The method for determining GCD
	def GCD(self, nums):

		#Sort the nums array from largest to smallest
		nums.sort()
		nums.reverse()
		print(nums)
		e = list(range (2))

		#Compare each to the next
		e[0], e[1] = nums.pop(0), nums.pop(1)
		
		while e[1] > 0:
			r = e[0] % e[1]
			e[0] = e[1]
			e[1] = r
			print(e[0], e[1])
			if e[1] == 1:
				print("\nThere are no common divisors\n")
				break
			if e[1] == 0:
				e[1] = nums[1]

		print(e[0])

i = inCommon()
			
