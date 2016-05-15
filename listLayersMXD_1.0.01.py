################################################################################
# Title:            listLayersMXD.py
# Description:      This script crawls a supplied directory and lists
#                   all the layers and Groupings in any MXD in that
#                   directory.
#
# Author:           Pete Smyth
# Date:             13th November 2014
#
# Required Modules: arcpy   (Installed with ArcGIS)
#
#                   os (native)
#
# Amendments:       1.0.00  Finalised minor errors and released
#                           (P. Smyth - 13/11/2014 11:32)
#
# Amendments:       1.0.01  Changed script to incorporate definition of
#							layers and Groupings
#                           (P. Smyth - 25/11/2014 10:13)
#
################################################################################

print "\n ######################## PROCESS STARTING ######################## "
print "Beginning directory scan"

import arcpy, os
from time import strftime, localtime
from arcpy import mapping

mypath = r'E:\Python\source\Dekho_4110'

# Define variable to store filenames (mxd's)
f = []
# Define variable to store layer/grouping names
s = []
# Define directory for the output file location
outfiledir = r'E:\Python\source\Dekho_4110'

# open file for writing to store the layer/groupings in
outfile = open(outfiledir + '\MXD_Listing_' + str(strftime("%Y%m%d_%H%M%S")) + ".csv",'w')

print "Creating list of valid MXD's"

# loop through the directory defined in mypath to create
# a list of mxd's and store them in the variable f
for (dirpath, dirnames, filenames) in os.walk(mypath):
	for file in filenames:
		if file.endswith('.mxd'):
			f.append(os.path.join(dirpath,file))

print "Listing Layers and Groups"

# loop through the entries in the variable f to list the
# layers and groupings for each and store them in the
# variable s
for filepath in f:
	mxd = mapping.MapDocument(filepath)
	for ly in mapping.ListLayers(mxd):
		try:
			val = ly.datasetName
			if val != "":
				# using the unicode string formatting below gets around
				# the EM dash and EN dash used in the layer names for City Planning
				s.append(u"{}".format(ly) + ",Layer")
		except:
			s.append(u"{}".format(ly) + ",Group")

print "Writing Layers and Groups into output file: " + outfiledir

# loop through the entries in the variable s to write them
# to the file defined by the variable outfile
for item in s:
	# using the unicode string encoding below gets around
	# the EM dash and EN dash used in the layer names for City Planning
	outfile.write(item.encode('utf-8') + "\n")

outfile.close()

print "\n ######################## PROCESS FINISHED ######################## "