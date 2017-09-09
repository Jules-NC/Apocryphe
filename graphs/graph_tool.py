# coding: utf-8
"""
Provides Graph object. You can do fun things and export this graph to gephi (if you want)
For complexity, V is the number of vertices and E the number of Edges
"""
import datetime    # For file name ==> no duplicates
import pickle


def is_cyclic(g):   # O(E + V)
    path = set()

    def visit(vertex):
        path.add(vertex)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                print(neighbour)    # NoBeouty
                return True
        path.remove(vertex)
        return False
    return any(visit(v) for v in g)

def construct_filename(folder='Misc', filename='dummy', extension='txt'):
    now = datetime.datetime.now()
    folder = '..ou/ressources/' + folder + '/'
    date = now.strftime("_%Y-%m-%d|%H:%M:") + str(now.second)
    filename = folder + filename + date + '.' + extension
    return filename

class Graph:  # O(1)
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self._it = 0    # For memory and complexity verification
        self.compute_type = None    # Used for edge addition: None for none, True for degree, False for summing

    def is_cyclic(self):
        return is_cyclic(self.edges)

    def compute_degree(self):   # O(V)
        if self.is_cyclic() is True:
            raise Exception('GraphEror', 'The graph is cyclic !')
        self.compute_type = True
        for k in self.vertices.keys():
            if self.vertices[k] == -1:
                self.degree(k, self.edges[k])

    def degree(self, vertice, edges):
        self._it += 1   # For memory and complexity verification
        if len(edges) == 0:
            self.vertices[vertice] = 0
            return 0
        recursives = max([self.degree(vert, self.edges[vert]) for vert in edges if self.vertices[vert] == -1],
                         default=0)
        non_recursives = max([self.vertices[vert] for vert in edges if self.vertices[vert] != -1])
        res = max((recursives, non_recursives)) + 1
        self.vertices[vertice] = res
        return res

    def compute_summing(self):    # O(V)
        if self.is_cyclic() is True:
            raise Exception('GraphEror', 'The graph is cyclic !')

        self.compute_type = False
        for k in self.vertices.keys():
            if self.vertices[k] == -1:
                self.summing(k, self.edges[k])

    def summing(self, vertice, edges):
        self._it += 1
        if len(edges) == 0:     # If LEAF
            self.vertices[vertice] = 1
            return 1
        res = 0
        for vert in edges:
            if self.vertices[vert] != -1:
                res += self.vertices[vert]
            else:
                res += self.summing(vert, self.edges[vert])
        res += 1
        self.vertices[vertice] = res
        return res

    def invert(self): #TODO comprendre ce truc
        self.reset_compute()
        new_edges = {source: [] for source in self.vertices.keys()}
        for source in self.vertices.keys():
            for target in self.edges[source]:
                new_edges[target].append(source)
        self.edges = new_edges

    def get_ordoned_vertices(self):    # O(2V)
        inv_map = [[v, k] for v, k in self.vertices.items()]
        inv_map.sort(key=lambda x: x[1], reverse=True)
        return inv_map

    def reset_compute(self):    # O(V)
        for vertice in self.vertices.keys():
            self.vertices[vertice] = -1

    def add_edge(self, a, b):
        if self.vertices.get(a) is not None:
            self.edges[a].append(b)
        else:
            self.vertices[a] = -1
            self.edges[a] = [b]
            if self.compute_type:
                self.degree(a, self.edges[a])
            if not self.compute_type:
                self.summing(a, self.edges[a])

    def delete_edge(self, a, b):
        if self.vertices.get(a) is None:
            return
        if b in self.edges[a]:
            self.edges[a].remove(b)

    def view(self):
        print('=====[GRAPH]=====')
        for key in self.vertices.keys():
            print(str(key), '(', self.vertices[key], ") => ", self.edges[key], sep="")
        print('======[END]======')

    def to_csv(self, filename='vizualization'):   # O(2V)
        file = construct_filename('Databases', filename, 'csv')

        edges = ((str(source), str(target), str(self.vertices[source]))     # Source/Target/Computed_value
                 for source in self.vertices for target in self.edges[source])

        with open(file, 'w') as f:
            f.write("Source,Target,Idk" + '\n')
            for edge in edges:
                f.write(edge[0] + ',' + edge[1] + ',' + edge[2] + '\n')

    def save(self):    # O(sef)
        file = construct_filename('Pickles','graph','pkl')
        with open(file, 'wb') as f:
            pickle.dump(self, f)

if __name__ == '__main__':

    from nltk.corpus import wordnet as wn
    # edges composition: {[node (int)]:[arcs (str)]}
    # vertices = {synset.name(): -1 for synset in wn.all_synsets()}
    # edges = {synset.name(): [target.name() for target in synset.hyponyms()] for synset in wn.all_synsets()}
    # edges['restrain.v.01'] = ['confine.v.03', 'control.v.02', 'hold.v.36']

    vertices = {'A':-1,
                'B':-1,
                'C':-1,
                'D':-1,
                'E':-1,
                'F':-1}
    edges = {'A':['B','C'],
             'B':[],
             'C':[],
             'D':['C', 'E'],
             'E':[],
             'F':['B', 'A', 'D']}

    print('CALCULATING...')

    gr = Graph(vertices, edges)
    gr.compute_degree()
    gr.to_csv('mots_avec_leurs_degré')     # TODO: régler cette probleme d'emplacement des fichiers
    gr.save()
    a = gr.get_ordoned_vertices()
    print(a[0])
