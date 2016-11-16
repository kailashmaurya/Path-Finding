# Path-Finding
Implementation of informed and uninformed search techniques on constrained graphs to find the path.

# Algorithms:

# Uninformed Algorithms: UCS, DFS and BFS
Uniform Cost Search : It does not involve the use of heuristics. It can solve any general graph for optimal cost. Uniform Cost Search as it sounds searches in branches which are more or less the same in cost.

Depth First Search : It starts at the root (selecting the source node as the root) and explores as far as possible along each branch before backtracking.

Breadth First Search : It starts at the root (selecting the source node as the root) and explores the neighbor nodes first, before moving to the next level neighbors.

# Informed Algorithm:
A-Star : It solves problems by searching among all possible paths to the solution (the goal node) for the one that incurs the smallest cost (least distance travelled, shortest time, etc.), and among these paths it first considers the ones that appears to lead most quickly to the solution, by using the heuristic function.

# How to run:
Make sure path_finding.py and input.txt are in the same directory before running the script file. When you run the path_finding.py file, it reads input.txt and applies path-finding algorithms on the input to look for the shortest path between source and destination node(specified in in the input file).
The script generates output.txt which holds the shortest path(sequence of nodes) between the source and the destination.

# Input Format:

&lt;ALGO&gt;<br>
&lt;START STATE&gt;<br>
&lt;GOAL STATE&gt;<br>
&lt;NUMBER OF GRAPH EDGE LINES&gt;<br>
&lt;GRAPH EDGE LINES&gt;<br>
&lt;NUMBER OF HEURISTIC LINES&gt;<br>
&lt;HEURISTIC LINES&gt;<br>

Where:<br>
&lt;ALGO&gt; is the algorithm to use and can be one of: “BFS”, “DFS”, “UCS”, “A*”.<br>
&lt;START STATE&gt; is the name of the starting node.<br>
&lt;GOAL STATE&gt; is the name of the goal node.<br>
&lt;NUMBER OF GRAPH EDGE LINES&gt; is the number of lines of graph edges.<br>
&lt;GRAPH EDGE LINES&gt; are lines of graph edges, describing the whole graph,<br>
Having format: &lt;NODE1&gt; &lt;NODE2&gt; &lt;TRAVEL TIME FROM NODE1 TO NODE2&gt;<br>
&lt;NUMBER OF HEURISTIC LINES&gt; is the number of lines of Heuristic values, one for each node.<br>
&lt;HEURISTIC LINES&gt; are lines of Heuristic information,<br>
Having the following format &lt;NODE&gt; &lt;ESTIMATED TIME FROM NODE TO GOAL&gt;<br>

# Output Format:
Any number of lines with the following format for each:<br>
&lt;NODE&gt; &lt;ACCUMULATED TRAVEL TIME FROM SOURCE NODE TO THIS NODE&gt;

# Runner:
You can test the script on multiple inputs using the Runner.py utility, Make sure you keep the 'cases' directory at the same level as Runner.py and path_finding.py<br>

# Graph Generators:
Two generators are included:<br>
1. Generates a large and dense graph consisting of 8K nodes
2. Generates random graphs based on 4 different parameters of the graph.
