import sys, csv, string

# Mapper

reader = csv.reader(sys.stdin, delimiter='\t')
specials = ',.!?:;"()<>[]#$=-/'
trans = string.maketrans(specials, ' '*len(specials))

for line in reader:
	if len(line) == 19:
		body = line[4]
		node_id = line[0]
		body = body.translate(trans)
		words = body.strip().split()
		for word in words:
			print "{0}\t{1}".format(word.lower(), node_id)

# Reducer

count = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisKey, thisValue = data_mapped
	if thisKey == "fantastically":
		print thisKey, "\t", thisValue

	if oldKey and oldKey != thisKey:
		if oldKey == "fantastic":
			print oldKey, "\t", count
		oldKey = thisKey
		count = 0

	oldKey = thisKey
	count += 1

if oldKey != None:
	print oldKey, "\t", count