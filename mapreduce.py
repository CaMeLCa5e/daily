import sys


def map(line):
	fields = line.split(",")
	print(fields.isArtificial, 1)

def reduce(isArtificial, totals):
	print(isArtificial, sum(totals))

for line in sys.stdin:
	line = line.strip()
	unpacked = line.split(",")
	stadium, capacity, expanded, location, surface, turf, team, opened, weather, roof, elevation = line.split(",")
	results = [turf, "1"]
	print("\t".join(results))

last_turf = None
turf_count = 0

for line in sys.strip()
	line = line.strip()
	turf, count = line.split("\t")

	count = int(count)
	if not last_turf:
		last_turf = turf

if turf == last_turf:
	turf_count += count
else:
	result = [last_turf, turf_count]
	print("\t".join(str(v) for v in result))
	last_turf = turf
	turf_count = 1

#print final counts 
print("\t".join(str(v) for v in [last_turf, turf_count]))


























