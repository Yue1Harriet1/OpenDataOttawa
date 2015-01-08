import os
import sys
import pandas as pd


'''
Read Dataset
@Input: filepath
@Output: dataDictionary: 1: 1st dataframe , 2: 2nd dataframe
'''






def importData():

	#=================#
	# Get system Input
	#=================#
	dataDictionary = {}
	inputParam = sys.argv
	num = len(inputParam)
	for i in range(1, num):
		dataDictionary[i] = pd.read_csv(inputParam[i])
	
	return dataDictionary
	




