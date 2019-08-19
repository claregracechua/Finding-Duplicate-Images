# refer to README.md for any reference materials and considerations.

# Solution referenced from: 
# https://www.pythoncentral.io/finding-duplicate-files-with-python/


# findDuplicateImages.py
# this program computes the hash of each file 
# in the directory,


import os
import sys
import hashlib


# this function calculates the MD5 hash of a file
# and returns a hash digest

def hashEachFile(path, blocksize = 65536):

    openfile = open(path, 'rb')

    # reads the image file in blocks
    buf = openfile.read(blocksize) 

    # uses MD5 hashing to
    hashing = hashlib.md5()

    while len(buf) > 0:
        hashing.update(buf)
        buf = openfile.read(blocksize)

    openfile.close()

    # returns the HEX digest of a given file
    return hashing.hexdigest()


# this function scans the directory, including
# any enclosed folders, for duplicate files

def findDuplicates(parentFolder):
	# List of duplicates in the following format:
	# {hash: [names of files]}

	duplicatesList = {}

	# walking through each folder
	for folderName, subFolders, fileList in os.walk(parentFolder):
		print('Scanning folder: ' + folderName)
		
		for fileName in fileList:

			# finds the path to each file
			path = os.path.join(folderName, fileName)

			# calculating the hash of each file
			fileHash = hashEachFile(path)

			# gets the file's hash, and add it into the duplicates list

			if fileHash in duplicatesList:
				duplicatesList[fileHash].append(path)
			else:
				duplicatesList[fileHash] = [path]

	# returns the list of duplicates

	return duplicatesList



# Joins two dictionaries

def joinDictionaries(dictionary1, dictionary2):

	# finding if the hash of two files are identical
	# iterates over dictionary2 and looks for any keys that 
	# are in dictionary 1

	for key in dictionary2.keys():

		if key in dictionary1:
			# if key in dictionary1, append values in dictionary2
			dictionary1[key] = dictionary1[key] + dictionary2[key]
		else:
			# if key does not exist, add to dictionary 1
			dictionary1[key] = dictionary2[key]




# prints the results of the duplicates check.


def printResults(dictionary1):

	# 
	results = list(filter(lambda x:len(x) > 1, dictionary1.values()))

	print('*')
	print('Scan completed')
	print('*')

	# if there are duplicates, print a list of duplicate files
	if len(results) > 0:
		
		print('Duplicates images were found!')
		print('These images were found to be identical in content.') 
		print('The names of the images could be different, but they have the same content.')
		print('*')


		for i in results:
			for subresult in i:
				print ('\t%s' % subresult)
			print('*')
		print('End of program!')
		print('*')
	else:
		print('No duplicates files found.')

# this function ensures that we can run this 
# script from the command line.


if __name__ == '__main__':

	# takes folder name as parameters
	# calls findDuplicateImages.py for every subfolder.
	if len(sys.argv) > 1:

		duplicatesList = {}
		folder = sys.argv[1]

		# checks whether the folder exists
		if os.path.exists(folder):
			joinDictionaries(duplicatesList, findDuplicates(folder))
		else:
			print('Either path is not valid, or folder does not exist. Please check again!')
			sys.exit()

		# print the output for this script	
		printResults(duplicatesList)

	else:
		# print this if no folder is specified
		print('To check for duplicates in on a folder, enter python findDuplicateImages.py foldername')
