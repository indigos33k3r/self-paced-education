import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
	if len(line) == 19:
		author_id = line[3]
		hour = int(line[8][11:13])
		print "{0}\t{1}".format(author_id, hour)

# Reducer

import sys

oldKey = None

hours = {}
for i in range(24):
	hours[i] = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisKey, thisValue = data_mapped

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", max(hours, key=hours.get)
		oldKey = thisKey
		for i in range(24):
			hours[i] = 0

	oldKey = thisKey
	hours[int(thisValue)] += 1

if oldKey != None:
	print oldKey, "\t", max(hours, key=hours.get)