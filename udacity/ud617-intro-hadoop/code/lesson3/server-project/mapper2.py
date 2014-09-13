import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		page = data[6]
		ip_address = data[0]
		print "{0}\t{1}".format(ip_address, page)