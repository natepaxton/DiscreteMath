"""
The purpose of this program is to build to arrays of 100 numbers each.
The numbers for each array will be random numbers between 1 and 200.  

The arrays will be displayed in their binary representations and the 
binary arrays will be compared to find the union and the intersection.

Once the union and intersection are found, the binary will be converted
back to decimal.  The output will show the intersection and union, as 
well as both input sets sorted.

The outputs are sorted using the native sort functions in Python.  The
outputs will all be sorted in ascending order.
"""
import random

class projectFive:

	def __init__(self):

		#Global variables
		self.aData = []
		self.bData = []

		#Instantiate the arrays
		A = self.irand(100, 200)
		B = self.irand(100, 200)

		#Convert the A data to binary
		for i in range(100):
			self.aData.append(self.bin(A[i], 8))

		#Print the A binary set
		print("\nA binary: \n")
		for i in range(100):
			print(self.aData[i])

		#Convert the B data to binary
		for i in range(100):
			self.bData.append(self.bin(B[i], 8))

		#Print the B binary set
		print("\nB binary: \n")
		for i in range(100):
			print(self.bData[i])

		#Print the sorted decimal sets
		A.sort()
		B.sort()
		print("\nSet A sorted: \n")
		print(A)
		print("\nSet B sorted: \n")
		print(B)

		self.abIntersect(A, B)
		self.abUnion(A, B)

	def irand(self, n, m):
		b = list(range(n))
		b = random.sample(range(m), n)
		return b

	def bin(self, n, m):
		a = []
		while n > 0:

			#Check for even numbers
			if n % 2 == 0:
				n = int(n/2)
				a.append(0)

			#Check for odds
			elif n % 2 == 1:
				n = int(n/2)
				a.append(1)

		#Check current length against specified length and add zeroes
		while len(a) < m:
		 	a.append(0)

		return list(reversed(a))

	def abIntersect(self, a, b):
		intersection = []

		#Nested for loops will handle comparison
		for i in range(len(a)):
			for j in range(len(b)):
				if a[i] == b[j]:
					intersection.append(a[i])
		
		print("\nThe intersection of A and B: \n")
		intersection.sort()
		print(intersection)

	def abUnion(self, a, b):
		union = []

		for i in range(len(a)):
			union.append(a[i])

		for i in range(len(b)):
			union.append(b[i])

		#Remove the duplicates from the union
		union = list(set(union))
		union.sort()
		print("\nThe union of A and B: \n")
		print(union)

p = projectFive()