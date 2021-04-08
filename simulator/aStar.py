## @file aStar.py
#
# @brief this file contains the a star algorithm to find shortest path
#

directions =  [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

class node():
    """!A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other): # comparison
        return self.position == other.position

    def __hash__(self):               #<-- added a hash method
        return hash(self.position) # not sure, need to google


def astar(maze, start, goal):
    """! Returns a list of tuples as a path from the given start 
    to the given goal in the given maze
    """
    if maze[start[0]][start[1]] == 1 or maze[goal[0]][goal[1]] == 1:
        return None

    # create start and goal node
    startNode = node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    goalNode = node(None, goal)
    goalNode.g = goalNode.h = goalNode.f = 0

    # initialize both open and closed list
    openList = []
    closedSet = set()

    # add the start node
    openList.append(startNode)

    # loop until you find the goal
    while len(openList) > 0:
        # get the current node
        currentNode = openList[0]
        currIdx = 0
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currIdx = index

        # pop current off open list, add to closed set
        openList.pop(currIdx)
        if currentNode.position in closedSet:
            continue # if already in closed set, continue
        else:
            closedSet.add(currentNode.position)

        # found the goal
        if currentNode == goalNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # return reversed path

        # generate children
        children = []
        for newPos in directions: # adjacent squares
            # get node position
            nodePos = (currentNode.position[0] + newPos[0], currentNode.position[1] + newPos[1])
            # make sure within range and walkable
            if nodePos[0] > (len(maze) - 1) or nodePos[0] < 0 or nodePos[1] > (len(maze[len(maze)-1]) -1) or nodePos[1] < 0 or maze[nodePos[0]][nodePos[1]] != 0:
                continue
            children.append(node(currentNode, nodePos))

        # loop through children
        for child in children:
            # child is on the closed set
            if child.position in closedSet:
                continue
            # create the f, g, and h values
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - goalNode.position[0]) ** 2) + ((child.position[1] - goalNode.position[1]) ** 2)
            child.f = child.g + child.h
            # child is already in the open list
            for x in openList:
                if child == x and child.g > x.g:
                    continue
            openList.append(child)
    return None
