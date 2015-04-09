

"""
graph parallel pattern  - iterating on the vertex of the neighbors


Collaborative Filtering 
 - alternative least stores 
 - stochastic gradient decent 
 - tensor factorization 

Structured Prediction
- loopy belief pattern 
- max product linear programs 
- gibbs sampling

Semi-supervised ML 
- graph ssl 
- CoEM

Community Detection 
- triangle-counting 
- K-core decomposition 
- K-Truss 

Graph Analytics 
- pageRank 
- personalized pageRank
- shortest path 
- graph coloring 

Classification
- neural Networks


pagerank, triangle-counting, connected components 
"""

class Graph[ VD, ED] {
	
}

graph.mapReduceTriplets(
	edge => Iterator(
		(edge.srcId, 1), 
		(edge.dstId, 1)),
	_ + _)






















