from fileio import file_to_2dlist
class node():
    """A node class for A* Pathfinding"""

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
    """Returns a list of tuples as a path from the given start to the given goal in the given maze"""
    if maze[start[0]][start[1]] == 1 or maze[goal[0]][goal[1]] == 1:
        return None

    # Create start and goal node
    startNode = node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    goalNode = node(None, goal)
    goalNode.g = goalNode.h = goalNode.f = 0

    # Initialize both open and closed list
    openList = []
    closedSet = set()

    # Add the start node
    openList.append(startNode)

    # Loop until you find the goal
    while len(openList) > 0:

        # Get the current node
        currentNode = openList[0]
        currIdx = 0
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currIdx = index

        # Pop current off open list, add to closed list
        openList.pop(currIdx)
        if currentNode.position in closedSet:
            continue
        else:
            closedSet.add(currentNode.position)     # <-- change append to add

        # Found the goal
        if currentNode == goalNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for newPos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            nodePos = (currentNode.position[0] + newPos[0], currentNode.position[1] + newPos[1])

            # Make sure within range
            if nodePos[0] > (len(maze) - 1) or nodePos[0] < 0 or nodePos[1] > (len(maze[len(maze)-1]) -1) or nodePos[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[nodePos[0]][nodePos[1]] != 0:
                continue

            # Create new node
            new_node = node(currentNode, nodePos)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child.position in closedSet:              # <-- remove inner loop so continue takes you to the end of the outer loop
                continue

            # Create the f, g, and h values
            child.g = currentNode.g + 1
            child.h = ((child.position[0] - goalNode.position[0]) ** 2) + ((child.position[1] - goalNode.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in openList:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            openList.append(child)
    return None
