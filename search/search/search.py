# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  ['South', s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """ 
    #IMPORTS
    from util import Stack

    #PRE-LIMINARY TESTING
     #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    dfs_stack = Stack()
    visited = []
    dfs_stack.push((problem.getStartState(), []))
    while not dfs_stack.isEmpty():
        xy, directions = dfs_stack.pop()
        if xy in visited:
            continue
        visited.append(xy)
        if problem.isGoalState(xy):
            return directions
        for xy, direction, _ in problem.getSuccessors(xy):
            if xy not in visited:
                dfs_stack.push((xy, directions + [direction]))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #IMPORTS
    from util import Queue
    bfs_queue = Queue()
    visited = []
    bfs_queue.push((problem.getStartState(), []))
    while not bfs_queue.isEmpty():
        xy, directions = bfs_queue.pop()
        if xy not in visited:
            visited.append(xy)
            if problem.isGoalState(xy):
                return directions
            for xy, direction, _ in problem.getSuccessors(xy):
                if xy not in visited:
                    bfs_queue.push((xy, directions + [direction]))
    
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    ucs_prio_q = PriorityQueue()
    visited = []
    pri = 0
    ucs_prio_q.push((problem.getStartState(), []), pri) #push priority and ucs
    dict = {problem.getStartState() : 0}
    while not ucs_prio_q.isEmpty():
        xy, directions = ucs_prio_q.pop()
        if problem.isGoalState(xy):
            return directions
        if xy not in visited:
            visited.append(xy)
            for xy_new, direction, prio in problem.getSuccessors(xy):
                value = dict.get(xy_new)
                if value is not None: 
                    if (dict[xy] + prio) < value:
                        ucs_prio_q.update((xy_new, directions + [direction]), dict[xy] + prio)
                        dict[xy_new] = dict[xy] + prio
                        continue
                    else:
                        continue
                else:
                    ucs_prio_q.push((xy_new, directions + [direction]), dict[xy] + prio) 
                    dict[xy_new] = dict[xy] + prio

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #starting aStarSearch
    from util import PriorityQueue
    visited = set()
    astar_prio_q = PriorityQueue()
    astar_prio_q.push((problem.getStartState(), []), 0)
    while not astar_prio_q.isEmpty():
        xy, directions = astar_prio_q.pop()
        if xy in visited:
            continue
        visited.add(xy)
        if problem.isGoalState(xy):
            return directions
        for xy_child, xy, stepCost in problem.getSuccessors(xy):
            if xy_child not in visited:
                astar_prio_q.push((xy_child,directions + [xy]),stepCost+problem.getCostOfActions(directions)+heuristic(xy_child, problem = problem))
    #util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
