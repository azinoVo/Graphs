def earliest_ancestor(ancestors, starting_node):
    # Write a function that, given the dataset and the ID of an individual in the dataset, 
    # returns their earliest known ancestor – the one at the farthest distance from the input 
    # individual. If there is more than one ancestor tied for "earliest", return the one with 
    # the lowest numeric ID. If the input individual has no parents, the function should return -1.
    pass
    # Ancestor = [(parent,child), (parent, child)]
    # test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    # Create the graph structure to visualize the relationships
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
           
