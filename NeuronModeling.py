''' Doc String 
	
	Neuron Modeling Module 

	Class Name: singleNeuron 

	Initialization inputs: 

		userInput (Numpy Array of Arrays)
		target (Numpy Array)
		transfer (Str)

	Methods
		Activation Methods:

			Sigmoid - Sigmoid Function

			Tanh - Hyperbolic Tangent function

			Inputs: 

				x (int or float)
				deriv (Bool)



'''





import numpy as np 
import pandas as pd 
class singleNeuron: 
		
	def __init__(self, userInput, target, transfer):

		self.input = userInput
		self.target = target 
		self.transfer = transfer

	''' Activation Methods  
		
		3 Activation Methods most widely used today. 

		Sigmoid
		Hyperbolic tangent 

		

		Intended to be internal methods to be called 
		at later times down the river. 


				'''

	def Sigmoid(self, x, deriv = False):

		if not deriv: 

			return 1/(1 + np.exp(-x))

		else: 

			return (Sigmoid(x)*(1 - Sigmoid(x)))

	def Tanh(self, x, deriv = False):

		if not deriv:

			return ((np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)))

		else:

			return (1 - (Tanh(x)**2))



		







if __name__ == '__main__':
	print(transferFunction(5, True))

