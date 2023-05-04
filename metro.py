class Vertex:
    name = 1

    def __init__(self):
        self._links = []
        self.name = Vertex.name
        Vertex.name += 1

    @property
    def links(self):
        return self._links

    def __repr__(self):
        return f'v{self.name}'


class Link:
    def __init__(self, v1: 'Vertex', v2: 'Vertex', distance=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = distance
        self.connection = (self._v1, self._v2)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'({self._v1}, {self._v2}, {self._dist})'

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v: 'Vertex'):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, new_link: 'Link'):
        v1 = new_link.v1
        v2 = new_link.v2

        alredy_connected = False
        new_svyaz = sorted(map(id, (v1, v2)))
        for link in self._links:
            svyaz = sorted(map(id, (link.v1, link.v2)))
            if new_svyaz == svyaz:
                alredy_connected = True
                break

        if not alredy_connected:
            self._links.append(new_link)




        if v1 not in self._vertex:
            self._vertex.append(v1)
        elif v2 not in self._vertex:
            self._vertex.append(v2)

    def find_path(self, v1, v2):
        self.otv = []
        self.recurs((v1, ), v2)
        """исправить равные пути"""
        path = {}
        for el in self.otv:
            path[el[-1]] = el[0]

        path = path[min(path)]
        connections = []

        for i in range(len(path) - 1):
            for el in self._links:
                if path[i] in [el.v1, el.v2] and path[i+1] in [el.v1, el.v2]:
                    connections.append(el)
                    break
        return path, connections




    def recurs(self, otv_vertexes: tuple['Vertex'], ver_end: 'Vertex', distance=0):
        if otv_vertexes[-1].name == ver_end.name:
            self.otv += [(otv_vertexes, distance)]

        connections = self.linked_vert(otv_vertexes[-1])
        for el in connections:
            if el[0] not in otv_vertexes:
                self.recurs(tuple(list(otv_vertexes) + [el[0]]), ver_end, distance + el[1])

        return



    def linked_vert(self, vert: 'Vertex'):
        links = list(filter(lambda x: vert in x.connection, self._links))
        return_links = []
        for el in links:
            if el.connection[0].name == vert.name:
                return_links += [(el.connection[1], el._dist)]
            else:
                return_links += [(el.connection[0], el._dist)]
            # print(el.connection[0].__class__)
        return return_links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return self.__repr__()


class LinkMetro(Link):
    def __init__(self, v1, v2, distance):
        super().__init__(v1, v2, distance)
        # self._v1 = v1
        # self._v2 = v2
        # self._dist = distance



