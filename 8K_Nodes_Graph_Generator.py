import random
nodes = ['A'] # Starts with the default root node
next_nodes = []
child_count = 1 # at the end of this utility this will hold the total number of nodes present in the graph
output = '' # at the end of this utility this will hold the full graph as a string
no_of_output_lines = 0

original_branch_factor = 4
branch_factor = 4 #start branch factor, it varies as the graph generation progresses
depth = 5 # the depth upto which expansion of nodes takes place, after this depth nodes start to converge
max_branch_factor = depth + branch_factor - 1
algorithm = 'A*' # possible values : A*, UCS, DFS and BFS
source = 'A' # the source node for path finding, Can be any node

# Starts branching out the nodes upto depth 'depth'
for i in range(depth):
    while nodes:
        parent = nodes.pop(0)
        for j in range(branch_factor):
            child = 'A' + str(child_count)
            output = output + parent + ' ' + child  + ' ' + str(random.randint(5, 35)) + '\n'
            no_of_output_lines = no_of_output_lines + 1
            next_nodes.append(child)
            child_count = child_count + 1
    nodes = next_nodes
    next_nodes = []
    branch_factor = branch_factor + 1
child_count = child_count - 1

# start converging in nodes from depth = depth+1 to 2*depth in the graph
nodes_considered = 0
for j in range(depth):
    for node in nodes:
        if nodes_considered % (max_branch_factor - j) == 0: 
            child_count = child_count + 1
        child = 'A' + str(child_count)
        output = output + node + ' ' + child  + ' ' + str(random.randint(5, 35)) + '\n'
        no_of_output_lines = no_of_output_lines + 1
        if nodes_considered % (max_branch_factor - j) == 0: 
            next_nodes.append(child)
        nodes_considered = nodes_considered + 1
    nodes = next_nodes
    next_nodes = []
output = algorithm + '\n' + source + '\n' + child + '\n' + str(no_of_output_lines) + '\n'+ output
no_sunday_traffic = int(child[1:]) + 1
heuristic_val = depth * 2
output = output + str(no_sunday_traffic)+ '\nA ' + str(heuristic_val) + '\n'
heuristic_val = heuristic_val -1
no_nodes = 1
child_count = 1

# Generate the Heuristic values for all the nodes
for i in range(depth * 2):
    if i  < depth:
        no_nodes = no_nodes * original_branch_factor # no of nodes at depth value(i + 1)
        original_branch_factor = original_branch_factor + 1
    elif i == depth:
        original_branch_factor = original_branch_factor - 1
        no_nodes = no_nodes / original_branch_factor
    elif i > depth:
        original_branch_factor = original_branch_factor - 1
        no_nodes = no_nodes / original_branch_factor # no of nodes at depth value(i + 1)
    print no_nodes
    for k in range(no_nodes):
        output = output + 'A' + str(child_count) + ' ' + str(random.randint(5, 35)) + '\n'
        child_count = child_count + 1
    heuristic_val = heuristic_val - 1

# writes the graph on an output file
output.rstrip('\n')
f_output = open('input.txt', 'w')
f_output.write(output)
f_output.close()