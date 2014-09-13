totalHits = 0
oldKey = None
mostHits = 0
bestKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisKey, thisValue = data_mapped

	if oldKey and oldKey != thisKey:
		if totalHits > mostHits:
			mostHits = totalHits
			bestKey = oldKey
			print oldKey, "\t", totalHits

		oldKey = thisKey
		totalHits = 0

	oldKey = thisKey
	totalHits += 1

if oldKey != None:
	print oldKey, "\t", totalHits