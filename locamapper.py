import sys

for line in sys.stdin
	line = line.strip()
	unpacked  = line.split(",")
	stadium, capacity, location, surface, turf, team, opened weather = line.split(",")
	results = [turf, "1"]
	print("\t".join(results))

	