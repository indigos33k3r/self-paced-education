import sys

total = 0.0
count = 0
for line in sys.stdin:
    data = float(line.strip())
    count += 1
    total += data
    print "{0}\t{1}".format(count, total)