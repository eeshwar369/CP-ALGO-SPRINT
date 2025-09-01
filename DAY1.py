# Day-01
# Let's Begin the Journney with DSU 
# This Journey is an adventure aslo to maintain python template for cp contest too
# 1. DSU implementataion by rank 

class DSU:
    def __init__(self,n):
        #  parent is wrong
        # self.parent=[1]*n 
        # correct is every node is parent to itself
        self.parennt[node]=list(range(n))
        self.rank=[0]*n 
    def find(self,node):
        # path compression helps so just implement it 
        #     if(node==self.parent[node]):
        #         return node 
        #     return self.parent[self.parent[node]] => This is also correct but T.C as no path compression
        # This is path compression
            if(node!=self.parent[node]):
                self.parent[node]=self.find(self.parent[node])
            return node
    
        
    def union(self,node1,node2):
        par1=self.find(node1)
        par2=self.find(node2)
        if(par1!=par2):
            # in order to minimize the size of tree 
            # let's joining the one with smaller rank to high rank
            # (hard to understand)
            # no worries try imaging 
            # always break and solve problmes
            # you were wrong compare root ranks not node ranks
            # if(self.rank[node1]<self.rank[node2]):
            #     self.parent[node2]=node1
            # elif(self.rank[node1]> self.rank[node2]):
            #     self.parent[node1]=node2 
            # else:
            #     self.parent[node1]=node2 
            #     self.rank[node2]+=1 
            if(self.rank[par1]<self.rank[par22]):
                self.parent[par2]=par1
            elif(self.rank[par1]> self.rank[par2]):
                self.parent[par1]=par2 
            else:
                self.parent[par1]=par2 
                self.rank[par2]+=1 

        
