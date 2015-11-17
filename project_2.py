'''
This program contains functions for the mathematical operators "implies" and "if and only if".
The class initiates by asking the user to choose between the implication operation or the 
if and only if operation.

The function for implies takes two inputs.  Either input could be true or false.  The function
will give the same results for the two inputs that the implication truth table displays.  
When the first argument is false, the result will be vacuously true.  The only case that 
returns false will be the case where the first statement is true and the second statement is
false.

The if and only if function determines whether both values are the same before returning the 
final outcome.  If both inputs match, the funtion returns true.  If they are mismatched, the
function returns false.

I abstracted two functions for use in both cases.  If the program is ran as a standalone, it 
will prompt the user to name and assign value to the statements.  The values are converted to 
upper and the first character is used to scrub user input.

'''

class iffImply:
	def __init__(self):

		#Prompt the user to choose implies or iff
		option = input("\nPlease choose Implication (M) or if and only if (F): ").upper()[0]
		
		#An array to house statement/truth pairs
		self.truths = []	

		#Check the user response for validity			
		if option == "M":
			print("\n--= Implication =--")

			#Get the attributes and push to array.
			self.getAttribs()

			#Instantiate the outcome variable
			outcome = True

			if self.truths[0][1] == True and self.truths[1][1] == False:
				outcome = False
			else:
				outcome = True
	
			print (str(self.truths[0][0]) + " implies " + str(self.truths[1][0]) + ": " + str(outcome))

		elif option == "F":
			print("\n--= If and Only If =--")

			#Get the attributes and push to array.
			self.getAttribs()

			#Instantiate the outcome variable
			outcome = True

			if self.truths[0][1] == True and self.truths[1][1] == True:
				outcome = True

			elif self.truths[0][1] == False and self.truths[1][1] == False:
				outcome = True

			else:
				outcome = False
	
			print (str(self.truths[0][0]) + " if and only if " + str(self.truths[1][0]) + ": " + str(outcome))

		#If the input is incorrect, display error and restart
		else:
			print("\nYou must choose either M or F")
			iffImply()

	#Abstracted for use in both options
	def pushTruth(self, stat, boolean):
		if boolean == "T":
			boolean = True
		elif boolean == "F":
			boolean = False
		self.truths.append((stat, boolean))

	#Abstracted for use in both options
	def getAttribs(self):
		for i in range(0, 2):

			#Using the index limits the input to one character
			stat = input("\nChoose a single character to represent statement " + str(i + 1) + ": ")[0]
			print ("\nStatement " + str(i + 1) + ": " + stat)
			truth = input("Is this statement true (T) or false (F)? ").upper()[0]

			#Determine the validity of the truth entry
			while truth != "T" and truth != "F" :
				print ("\nThe statement must be true (T) or false (F)")
				truth = input("\nIs this statement true (T) or false (F)? ").upper()[0]		

			self.pushTruth(stat, truth)

#Instantiate a table to call the function
iffy = iffImply()
input("\nPress the enter key to exit")