'''
This class will prompt a user for a number of statements, 
titles for those statements (P, Q, R, ...), and construct 
a truth table for the specified number of statements.  

The number of outcomes will be determined by raising two 
to the number of statements.

Once the number of rows has been determined, each row is 
iterated over.  During each iteration, the number of statements
is iterated over to determine a value to use for evaluating T/F.  
One is added to the value of the statement position because it is 
a zero based array.

The number of possible outcomes divided by two is raised to the 
power of the statement index plus one (s + 1).  Floor division is used
to determine if the result leaves a remainder when divided by the index
of the "truth" (t).  The result of that operation is operated on by
a modulo 2 (%2) to determine if it's evenly divisible by 2.

If the end result of the last operation is equal to zero, a truthy 
value is assigned to the entry.  If the operation renders a remainder, false
is assigned.  

The algorithm works because a truth table is a binary system in essence.  
Everything can be expanded by raising two exponentially, and there can only
be two outcomes, T or F.
'''
		
class truthTable:
	def __init__(self):

		#An empty array to contain statements
		self.statements = [];

		#Prompt the user for the number of statements
		numStats = int(input("How many statements would you like to enter? "))

		#Iterate over the statements, adding each title to the
		#statements array
		for s in range(numStats):
			state = input("Enter statement title " + str(s + 1) + ": ")
			self.statements.append(state)

		#Variable containing the line that goes between
		#rows in the truth table
		line = "+" + ("---+" * len(self.statements))

		#Display a simple header for the truth table
		print ("\n") 
		print ("Truth Table for " + str(numStats) + " statements: \n")
		print (line)
		print ("|", end=' ')
		for statement in self.statements:
			print (statement + " |", end=' ')
		print ("\n" + line)
		
		#Determine the number of truths by raising
		#two to the number of statements
		numTruths = int(2 ** len(self.statements))	

		#Iterate over the number of rows
		for t in range(numTruths):
			truth = "|"
			print (line)

			#Iterate over the number of statements for each row
			for s in range(numStats):
				if (t//(numTruths/2**(s+1)))%2==0:
					truth = truth + " T |"
					continue
				truth = truth + " F |"
			print (truth)
		print (line)

#Instantiate a table to call the function
table = truthTable()
input("\nPress the enter key to exit")