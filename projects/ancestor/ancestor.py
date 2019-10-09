# Build the Queue
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Build the Graph
class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

def earliest_ancestor(ancestors, starting_node):
    # Write a function that, given the dataset and the ID of an individual in the dataset, 
    # returns their earliest known ancestor – the one at the farthest distance from the input 
    # individual. If there is more than one ancestor tied for "earliest", return the one with 
    # the lowest numeric ID. If the input individual has no parents, the function should return -1.

    # Ancestor = [(parent,child), (parent, child)]
    # test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    # Create the graph structure to visualize the relationships
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # Build edges in reverse to display the correct relationship
        graph.add_edges(pair[1], pair[0])

        # Create the queue
        qq = Queue()
        qq.enqueue([starting_node])

        max_path_length = 1
        earliest_ancestor = -1

         # Then search the graph for the farthest common ancestor
        # The earliest ancestor is farthest node with a connection to that starting node
        # We are checking the CHILD slot or starting_node to see if it has parents and store those possibilities
        #  # will require multiple lists to store the paths 
            # since ancestors can be tied for longest path - return the lower numbered ancestor if tied
            # Example, for node 6
                # we store the path(3) 
                    # Correct for path(3) is (3, 1, 10)
                    # path(3) then has another branching path(3,2)
                # and path(5) separately and then compare it at the end
                # paths are stored as paths=[(1,2,4),(1,2,4,6),(1,2,3)]
                # check for longest/if tied account return smallest

        while qq.size() > 0:
            path = qq.dequeue()
            v = path[-1]

            if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
                earliest_ancestor = v
                max_path_length = len(path)

            for neighbor in graph.vertices[v]:
                path_copy = list(path)
                path_copy.append(neighbor)
                qq.enqueue(path_copy)

           
