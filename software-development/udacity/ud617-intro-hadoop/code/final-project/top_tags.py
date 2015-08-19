# Mapper

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
	if len(line) == 19:
		node_id = line[0]
		node_type = line[5]
		tagnames = line[2]
		if node_type == "question":
			print "{0}\t{1}".format(node_id, tagnames)

# Reducer

import sys

tags = {}

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	node_id, tagnames = data_mapped

	for tag in tagnames.strip().split():
		if tag not in tags:
			tags[tag] = 1
		else:
			tags[tag] += 1

top10 = sorted(tags, key=tags.get, reverse=True)[:10]
for tag in top10:
	print tag, "\t", tags[tag]