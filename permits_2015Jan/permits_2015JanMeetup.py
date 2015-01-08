
from urllib2 import urlopen
from StringIO import StringIO
import pandas as pd
import readData






class AnalyzePermits:

	def __init__(self):

		self.dataDictionary = {}
		self.dataFrame = None



	'''
	==========================
		Main Method
	==========================
	'''
	def runAnalysis(self):

		#=================#
		# Import Data     #
		#=================#
		self.dataDictionary = readData.importData()
		dlist = list(self.dataDictionary.values())
		self.dataFrame = pd.concat(dlist)
		print self.dataFrame.describe()
		
		

if __name__ == "__main__":
	p = AnalyzePermits()
	p.runAnalysis()