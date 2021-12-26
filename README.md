# OOP - Ex3
In this task we were required to create a structure that will present a graph.
We were given some interfaces that we have implemented.
In this project we need to calculate algorithms on the graph that we created (center, shortest path between two nodes, TSP, ...).
Eventually, we created a GUI that draws the graph.

# Shortest Path Algorithm logic
The algorithm logic is based on the following:
1) copying the graph and creating a list of NodeData.
2) sending the source and dest nodes to the Shortest Path Distance Algorithm.
2) if it won't return us -1, that means that there's a track between them.
3) we will transpose the copied graph.
4) now we will start from the dest node, add it to the list, and check for his neighbors which neighbor weight + edge weight = dest weight.
5) the one node that will give us the equality is our next node, we will add it to the list, and now check on this node, the previous question.
6) we will continue doing that until we will get to the source node.
7) in the end, we will reverse the list.
8) checking the weight of the dest node.

# Center Algorithm logic
The algorithm logic is based on the following:
1) going through all of the graph nodes.
2) for each node we will perform the Dijkstra Algorithm.
3) find the maximum weight relative to all other nodes.
4) going to the next node and doing the same.
5) find the minimum of the maximum weights.
6) the one node that gave us the minimum is the center of the graph.

# TSP Algorithm logic
The algorithm logic is based on the following:
1) creating an ArrayList that will present the sequence of the given nodes that we will need to perform shortest path.
2) going through all of the nodes in the given list.
3) creating an ArrayList that will present an optional sequence of the given nodes.
4) adding the node to the optional ArrayList.
5) sending the node to a help function (tspHelp) and it will return us the next node (from the given nodes) that we would like to move to.
6) add the next node to the optional ArrayList.
7) keep sending to tspHelp and finding the next node until we did it size of the given nodes list.
8) going through the optional ArrayList, and calculating the shortest path dist in this list order.
9) going to the next given node and doing the above.
10) the minimum shortest path dist will be the final ArrayList.
11) sending the final ArrayList to the Shortest Path algorithm and return this list.

# Project structure
Class name | description
--- | ---
Point2D | present a location of graph node.
Node_Data | present a graph node.
Edge_Data | Present a graph edge.
DiGraph | Present a graph.
GraphAlgo | Present a class to perform algorithms on a graph.

# UML
![image](https://user-images.githubusercontent.com/63747865/147159766-86e79915-6cf6-47c0-9be4-bd3bf40d2fea.png)

# How to run
1. Install python 3 on your pc.
2. Download (clone) the project.
3. Run the main class and change the graph path to the path that you want.

# Project creators
Matan Yarin Shimon & Yarin Hindi
