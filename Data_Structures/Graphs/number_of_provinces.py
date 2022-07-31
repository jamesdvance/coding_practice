"""
 Number of Provinces

 There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Rephrase: count the number of disjoint sets 

Input: list of integer lists 
Output integer 

Will try to use Union Find since its the algo I'm studying

[[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],
[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]

-> 3

Current code spit out 4
"""

class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

    	qu = QuickUnion(max(len(isConnected),len(isConnected[0])))
    	for n in range(len(isConnected)):
    		for m in range(n+1, len(isConnected[0])):# was counting nodes connected to themselves.
    			if isConnected[n][m]==1:
    				qu.union(n,m)

    	return qu.getCount()

class QuickUnion:

	def __init__(self,size):
		self.root = [i for i in range(size)]
		self.rank = [1] * size 
		self.count = size

	def find(self,x):
		if self.root[x] == x:
			return x 
		self.root[x] = self.find(self.root[x])
		return self.root[x]

	def union(self,x,y):
		rootX = self.find(x)
		rootY = self.find(y)
		if rootX != rootY:
			if self.rank[rootX] > self.rank[rootY]:
				self.root[rootY] = self.root[rootX]
			elif self.rank[rootX] < self.rank[rootY]:
				self.root[rootX] = self.root[rootY]
			else:
				self.root[rootY] = self.root[rootX]
				self.rank[rootX] +=1

			self.count-=1 # unioned two nodes, total goes down by 1

	def getCount(self):
		return self.count

	def connected(self,x,y):
		return self.find(x) == self.find(y)