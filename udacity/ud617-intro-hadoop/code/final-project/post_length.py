# Mapper

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)

for line in reader:
	if len(line) == 19:
		node_id = line[0]
		body = line[4]
		node_type = line[5]
		parent_id = line[6]
		if node_type == "question":
			print "{0}\t{1}\t{2}".format(node_id, node_type, len(body))
		elif node_type == "answer":
			print "{0}\t{1}\t{2}".format(parent_id, node_type, len(body))

# Reducer

import sys

oldKey = None
totalAnswerLength = 0
postLength = 0
numAnswers = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 3:
		continue

	thisKey, node_type, len_body = data_mapped

	if oldKey and oldKey != thisKey:
		if numAnswers != 0:
			print oldKey, "\t", postLength, "\t", totalAnswerLength / numAnswers
		else:
			print oldKey, "\t", postLength, "\t", 0
		oldKey = thisKey
		totalAnswerLength = 0
		postLength = 0
		numAnswers = 0

	oldKey = thisKey
	if node_type == "question":
		postLength = float(len_body)
	elif node_type == "answer":
		totalAnswerLength += float(len_body)
		numAnswers += 1

if oldKey != None:
	if numAnswers != 0:
		print oldKey, "\t", postLength, "\t", totalAnswerLength / numAnswers
	else:
		print oldKey, "\t", postLength, "\t", 0
