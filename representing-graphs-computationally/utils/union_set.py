class UnionSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeSet(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def union(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if(self.rank[x] > self.rank[y]):
            self.parent[y] = x
        else:
            self.parent[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] = self.rank[y] + 1

    def findSet(self, x):
        if self.parent[x] != x:
            return self.findSet(self.parent[x])
        return x
    