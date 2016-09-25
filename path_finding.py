from operator import attrgetter
graph = {}
heuristic = {}
algorithm = ''
source = ''
dest = ''

class Node(object):
    def __init__(self, state):
        self.state = state
        self.path_cost = 0
        self.parent = None

    def attach_to_parent(self, parent):
        self.parent = parent

    def calculate_pathcost(self, parent, cost=0):
        if cost != 0:
            self.path_cost = parent.path_cost + cost
        else:
            self.heuristic_value = self.path_cost + heuristic[self.state]

    def goal_test(self):
        if dest == self.state: return True
        return False

    def in_frontier(self, frontier):
        try:
            index = [node.state for node in frontier].index(self.state)
            return True, index
        except ValueError:
            return False, 0

def init_problem():
    global algorithm, graph, heuristic, source, dest	
    with open('input.txt') as f_input:
        file = list(f_input)
    f_input.close()
    algorithm = file[0].rstrip('\n')
    source = file[1].rstrip('\n')
    dest = file[2].rstrip('\n')
    no_traffic_lines = int(file[3].rstrip('\n')) + 4
    for traffic_line in file[4:no_traffic_lines]:
        traffic_line = traffic_line.rstrip('\n').split(' ')
        if traffic_line[0] not in graph:
            graph[traffic_line[0]] = []
        graph[traffic_line[0]].append({traffic_line[1]:int(traffic_line[2])})
    no_sunday_traffic = int(file[no_traffic_lines].rstrip('\n'))
    for sunday_traffic in file[no_traffic_lines + 1 : no_traffic_lines + no_sunday_traffic + 1]:
        sunday_traffic = sunday_traffic.rstrip('\n').split(' ')
        heuristic[sunday_traffic[0]] = int(sunday_traffic[1])

def write_output(output):
    f_output = open('output.txt', 'w')
    f_output.write(output)
    f_output.close()

def trace_path(goal_node):
    path = []
    while goal_node:
        path.append(goal_node.state + ' ' + str(goal_node.path_cost))
        goal_node = goal_node.parent
    path = '\n'.join(path[::-1])
    path.rstrip('\n')
    write_output(path)

def expand_node(node):
    """
    returns list of next states possible from current state in node
    returns empty list if next states not possible
    """
    next_states = []
    if node.state in graph:
        for i, neighbour in enumerate(graph[node.state]):
            child = Node(neighbour.keys()[0])
            child.path_cost = neighbour.values()[0] + node.path_cost
            child.rank = i
            next_states.append(child)
    return next_states

def BFS():
    explored = set()
    frontier = []
    root = Node(source)
    if root.goal_test(): write_output(source + ' 0')
    frontier.append(root)
    while frontier:
        node_to_expand = frontier.pop(0)
        explored.add(node_to_expand.state)
        child_nodes = expand_node(node_to_expand)
        for child in child_nodes:
            infrontier, index = child.in_frontier(frontier)
            if child.state not in explored and not infrontier:
                child.attach_to_parent(node_to_expand)
                child.calculate_pathcost(node_to_expand, 1)
                if child.goal_test(): return child
                frontier.append(child)
    return None

def DFS():
    explored = set()
    frontier = []
    root = Node(source)
    if root.goal_test(): write_output(source + ' 0')
    frontier.append(root)
    while frontier:
        node_to_expand = frontier[-1]
        del frontier[-1]
        explored.add(node_to_expand.state)
        child_nodes = expand_node(node_to_expand)
        for child in reversed(child_nodes):
            infrontier, index = child.in_frontier(frontier)
            if child.state not in explored and not infrontier:
                child.attach_to_parent(node_to_expand)
                child.calculate_pathcost(node_to_expand, 1)
                if child.goal_test(): return child
                frontier.append(child)
    return None

def UCS():
    explored = {}
    frontier = []
    root = Node(source)
    if root.goal_test(): write_output(source + ' 0')
    frontier.append(root)
    while frontier:
        node_to_expand = frontier.pop(0)
        if node_to_expand.goal_test(): return node_to_expand
        explored[node_to_expand.state] = node_to_expand
        child_nodes = expand_node(node_to_expand)
        flag = False
        flag_reorder = False
        for child in child_nodes:
            infrontier, index_infrontier = child.in_frontier(frontier)
            if child.state not in explored and not infrontier:
                child.attach_to_parent(node_to_expand)
                frontier.append(child)
                flag = True
            elif infrontier and child.path_cost < frontier[index_infrontier].path_cost:
                child.attach_to_parent(node_to_expand)
                frontier[index_infrontier] = child
                flag = True
            elif child.state in explored and child.path_cost < explored[child.state].path_cost:
                child.attach_to_parent(node_to_expand)
                frontier.append(child)
                del explored[child.state]
                flag = True
                flag_reorder = True
        if flag: frontier.sort(key=attrgetter('path_cost'))
        if flag_reorder:
            do_reordering = False
            sameparent_dict = {}
            for node in frontier:
                if node.parent.state in sameparent_dict:
                    sameparent_dict[node.parent.state].append(node)
                    do_reordering = True
                else:
                    sameparent_dict[node.parent.state] = [node]
            if do_reordering:
                for parent, value in sameparent_dict.iteritems():
                    if len(value) > 1:
                        value.sort(key=attrgetter('rank'))
                        value.sort(key=attrgetter('path_cost'))
                for i, node in enumerate(frontier):
                    frontier[i] = sameparent_dict[node.parent.state].pop(0)
    return None

def A_Star():
    explored = {}
    frontier = []
    root = Node(source)
    root.heuristic_value = heuristic[root.state]
    if root.goal_test(): write_output(source + ' 0')
    frontier.append(root)
    while frontier:
        node_to_expand = frontier.pop(0)
        if node_to_expand.goal_test(): return node_to_expand
        explored[node_to_expand.state] = node_to_expand
        child_nodes = expand_node(node_to_expand)
        flag = False
        flag_reorder = False
        for child in child_nodes:
            infrontier, index_infrontier = child.in_frontier(frontier)
            child.calculate_pathcost(node_to_expand)
            if child.state not in explored and not infrontier:
                child.attach_to_parent(node_to_expand)
                frontier.append(child)
                flag = True
            elif infrontier and child.path_cost < frontier[index_infrontier].path_cost:
                child.attach_to_parent(node_to_expand)
                frontier[index_infrontier] = child
                flag = True
            elif child.state in explored and child.path_cost < explored[child.state].path_cost:
                child.attach_to_parent(node_to_expand)
                frontier.append(child)
                del explored[child.state]
                flag = True
                flag_reorder = True
        if flag: frontier.sort(key=attrgetter('heuristic_value'))
        if flag_reorder:
            do_reordering = False
            sameparent_dict = {}
            for node in frontier:
                if node.parent.state in sameparent_dict:
                    sameparent_dict[node.parent.state].append(node)
                    do_reordering = True
                else:
                    sameparent_dict[node.parent.state] = [node]
            if do_reordering:
                for parent, value in sameparent_dict.iteritems():
                    if len(value) > 1:
                        value.sort(key=attrgetter('rank'))
                        value.sort(key=attrgetter('heuristic_value'))
                for i, node in enumerate(frontier):
                    frontier[i] = sameparent_dict[node.parent.state].pop(0)
    return None

init_problem()
if algorithm == 'BFS':
    goal_node = BFS()
elif algorithm == 'DFS':
    goal_node = DFS()
elif algorithm == 'UCS':
    goal_node = UCS()
elif algorithm == 'A*':
    goal_node = A_Star()
else:
    print 'Unknown Algorithm'
if goal_node:
    trace_path(goal_node)