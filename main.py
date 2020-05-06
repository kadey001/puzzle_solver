"""
Kelton Adey
Eight-Puzzle Using:
1. Uniform Cost Search
2. A* with Misplaced Tile Heuristic
3. A* with the Eucledian Distance Heuristic
"""

import sys, heapq, utility
from state import State

class Node():
   def __init__(self, state, parent_node):
      self.state = state
      self.parent_node = parent_node

def graph_search(initial_state, heuristic, algorithm):
   if initial_state.is_goal():
      return 'Solved'
   #Set intial state's heuristic and algorithm type so operations are performed correctly
   initial_state.heuristic = heuristic
   initial_state.algorithm = algorithm
   max_frontier_size, nodes_expanded = 0, 0
   visited = []
   parent_node = Node(initial_state, initial_state)
   frontier = []
   heapq.heappush(frontier, (0, parent_node))

   while frontier:
      #Upade max_frontier_nodes
      max_frontier_size = max(len(frontier), max_frontier_size)

      #pop off cheapest costing node from heapq
      cheapest_element = heapq.heappop(frontier)
      node = cheapest_element[1]
      nodes_expanded += 1

      if not node.state.current_state in visited:
         visited.append(node.state.current_state)
         if node.state.is_goal():
            #Finished, output results
            print('Goal!!!\n')
            print('To solve this problem the search algorithm expanded a total of {} nodes'.format(nodes_expanded))
            print('The maximum number of nodes in the queue at any one time: {}\n'.format(max_frontier_size))
            output_optimal(initial_state, parent_node, node)
            return 'Success'

         print('The best state to expand with g(n) = {} h(n) = {} is...'.format(node.state.g_cost, node.state.h_cost))
         node.state.print_state()
         print('Expanding this node...')

         moves = node.state.get_moves()
         for state in moves:
            new_node = Node(state, node)
            if algorithm is 'a_star':
               heapq.heappush(frontier, (state.g_cost + state.h_cost, new_node))
            else: 
               heapq.heappush(frontier, (state.g_cost, new_node))
   return 'Failure'

def create_custom_puzzle():
   """
   Prompts user to create a custom starting puzzle
   Puzzle should be formatted as:
   [
      [A1, A2, Ak...],
      [B1, B2, Bk...],
      [C1, C2, Ck...],
      [j1, j2, jk...]
      ...
   ]
   """
   print('Enter your puzzle, use a zero to represent the blank space and use spaces/tabs between numbers')
   print('Enter row 1:\n')
   rows = []
   rows.append([int(x) for x in sys.stdin.readline().split()])
   for i in range(1,len(rows[0])):
      print('Enter row {}:\n'.format(i + 1))
      rows.append([int(x) for x in sys.stdin.readline().split()])
   return rows

def create_default_puzzle():
   """
   Creates a default starting puzzle
   """
   print('Select Default Puzzle')
   print('1: Trivial')
   print('2: Very Easy')
   print('3: Easy')
   print('4: Doable')
   print('5: Oh Boy')
   selection = input()
   puzzles = [
      [[1, 2, 3], [4, 5, 6], [7, 8, 0]],
      [[1, 2, 3], [4, 5, 6], [7, 0, 8]],
      [[1, 2, 0], [4, 5, 3], [7, 8, 6]],
      [[0, 1, 2], [4, 5, 3], [7, 8, 6]],
      [[8, 7, 1], [6, 0, 2], [5, 4, 3]],
   ]
   return puzzles[int(selection) - 1]

def output_optimal(initial_state, parent_node, result_node):
   #Finished, output results
   optimal_solution = []

   while not result_node is parent_node:
      optimal_solution.append(result_node.state)
      result_node = result_node.parent_node

   print('==================')
   print('Final Optimal Solution Trace')
   initial_state.print_state()

   for index in range(len(optimal_solution) - 1, 0, -1):
      state = optimal_solution[index]
      print(state.last_move)
      state.print_state()
   pass

   print('Finished')
   optimal_solution[0].print_state()
   return 

def algorithm_selection(state):
   print('Enter your choice of algorithm')
   print('1: Uniform Cost Search')
   print('2: A* with Misplaced Tile Heuristic')
   print('3: A* with the Eucledian Distance Heuristic')
   print('4: [Back]')
   selection = input()
   if int(selection) is 2:
      print('A* with Misplaced Tile Heuristic')
      heuristic = 'misplaced_tiles'
      algorithm = 'a_star'
      result = graph_search(state, heuristic, algorithm)
      pass
   elif int(selection) is 3:
      print('A* with the Eucledian Distance Heuristic')
      heuristic = 'eucledian'
      algorithm = 'a_star'
      result = graph_search(state, heuristic, algorithm)
      pass
   elif int(selection) is 4:
      return False
   else:
      print('Uniform Cost Search')
      heuristic = 'eucledian'
      algorithm = 'uniform'
      result = graph_search(state, heuristic, algorithm)

   print(result)

   return True

def main():
   print('Welcome to Kelton\'s (ID: 861234792) 8 puzzle solver')
   selection = True
   while selection:
      selection = input('Type "1" to use a default puzzle, "2" to enter your own, and "0" to Exit\n')
      if int(selection) is 2:
         puzzle_set = create_custom_puzzle()
      elif int(selection) is 0:
         return
      else:
         print('Default Puzzle')
         puzzle_set = create_default_puzzle()

      print('Puzzle Selected')
      utility.set_position_dict(len(puzzle_set))
      state = State(puzzle_set, 0, len(puzzle_set), first_state=True)
      state.print_state()

      keep_running = True
      while(keep_running):
         keep_running = algorithm_selection(state)

if __name__ == "__main__":
   main()
