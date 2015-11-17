'''
The purpose of this program is to convert an integer to a binary list with a specified 
number of values.  The inputs will be determined by the user.  If the user-selected 
number of values is less than the number of values required to give the binary 
representation, the program will output an array of values with the minimal length
required instead of the user-selected length.

The bin function performs the binary conversion operation by evenly dividing the input 
number repeatedly until it is equal to zero.  The ones and zeroes are appended to the 
output array.  The array is then reversed, so that it is right justified.  The final 
display is the right justified array.

'''
class intToBinary:

	def __init__(self):

		#Global variables
		self.n = 0
		self.a = []

		#Prompt the user for inputs
		self.n = int(input("\nEnter an integer to be converted: "))
		self.aLength = input("\nEnter the number of places to be converted: ") 

		#Convert to binary
		self.bin(self.n)

		#Check current length against specified length and add zeroes
		while len(self.a) < int(self.aLength):
			self.a.append(0)			

		#Reverse the order and display
		print ("\n" + str(list(reversed(self.a))))

	def bin(self, n):
		while self.n > 0:

			#Check for even numbers
			if self.n % 2 == 0:
				self.n = int(self.n/2)
				self.a.append(0)

			#Check for odds
			elif self.n % 2 == 1:
				self.n = int(self.n/2)
				self.a.append(1)

i = intToBinary()