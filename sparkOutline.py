val oldestFollowerAge = graph
	.mrTriplets(
		e => (e.dst.id, e.src.age),)