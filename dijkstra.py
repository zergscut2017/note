class Vertex(object):
    def __init__(self, v):
        self.adj = {}
        self.known = False
        self.dist = float(inf)
        self.path = None

class Graph(object):
    def __init__(self):
        self.vertexlist = []
        self.adj = []
        self.adjweight = {}
        
    def buildgraph_wuxiang(self, graph):
        for key in graph:
            self.vertexlist.append(key)
            self.adj.append(graph[key])

    def buildgraph_youxiang(self, graph):
        for key in graph:
            self.vertexlist.append(key)
            self.adj.append(graph[key])        

    def printgraph(self):
        print self.vertexlist
        print self.adj

if __name__ == '__main__':
    graph_list = { "s1": [ "s2", "s3" ],
                   "s2": [ "s3", "s4" ],
                   "s3": [ "s4" ],
                   "s4": [ "" ]

    }

    graph_dict = {  "s1":{"s1": 0, "s2": 2, "s10": 1, "s12": 4, "s5":3},
                    "s2":{"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5":2},
                    "s10":{"s1": 2, "s2": 1, "s10": 0, "s12":1, "s5":4},
                    "s12":{"s1": 3, "s2": 5, "s10": 2, "s12":0,"s5":1},
                    "s5":{"s1": 3, "s2": 5, "s10": 2, "s12":4,"s5":0},
    }

    graph1 = Graph()
    graph1.buildgraph_wuxiang(graph_list)
    graph1.printgraph()
    print('****************************')
    graph_youxiang = Graph()
    graph_youxiang.buildgraph_youxiang(graph_dict)
    graph_youxiang.printgraph()




