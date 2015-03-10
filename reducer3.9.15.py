import sys

last_turf = None
turf_count = 0

for line in sys.stdin:
	
	line = line.strip()
	turf, count = line.split("/t")

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

print("\t".join(str(v) for v in [last_turf, turf_count]))

