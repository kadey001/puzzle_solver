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

def uniform_cost_search(initial_state):
   initial_state.heuristic = 'eucledian'
   initial_state.algorithm = 'uniform'
   max_frontier_size, nodes_expanded = 0, 0
   visited = []
   #(g_cost, node, path)
   parent_node = Node(initial_state, initial_state)
   frontier = []
   heapq.heappush(frontier, (0, parent_node))

   while frontier:
      #Upade max_frontier_nodes
      max_frontier_size = max(len(frontier), max_frontier_size)

      #pop off cheapest node
      cheapest_element = heapq.heappop(frontier)
      node = cheapest_element[1]
      nodes_expanded += 1

      if not node.state.current_state in visited:
         visited.append(node.state.current_state)
         if node.state.h_cost is 0:
            #Finished, output results
            output_results(initial_state, parent_node, node, nodes_expanded, max_frontier_size)
            return

         moves = node.state.get_moves()
         for state in moves:
            new_node = Node(state, node)
            heapq.heappush(frontier, (state.g_cost, new_node))

   return 'Failure'

def a_star_tile_heuristic_search(initial_state):
   initial_state.heuristic = 'misplaced_tiles'
   initial_state.algorithm = 'a_star'
   max_frontier_size, nodes_expanded = 0, 0
   visited = []
   #(g_cost, node, path)
   parent_node = Node(initial_state, initial_state)
   frontier = []
   heapq.heappush(frontier, (initial_state.h_cost, parent_node))

   while frontier:
      #Upade max_frontier_nodes
      max_frontier_size = max(len(frontier), max_frontier_size)

      #pop off cheapest node
      cheapest_element = heapq.heappop(frontier)
      node = cheapest_element[1]
      nodes_expanded += 1

      if not node.state.current_state in visited:
         visited.append(node.state.current_state)
         if node.state.h_cost is 0:
            #Finished, output results
            output_results(initial_state, parent_node, node, nodes_expanded, max_frontier_size)
            return 

         moves = node.state.get_moves()
         for state in moves:
            new_node = Node(state, node)
            heapq.heappush(frontier, (state.g_cost + state.h_cost, new_node))
   pass

def a_star_eucledian_dist_search(initial_state):
   initial_state.heuristic = 'eucledian'
   initial_state.algorithm = 'a_star'
   max_frontier_size, nodes_expanded = 0, 0
   visited = []
   #(g_cost, node, path)
   parent_node = Node(initial_state, initial_state)
   frontier = []
   heapq.heappush(frontier, (initial_state.h_cost, parent_node))

   while frontier:
      #Upade max_frontier_nodes
      max_frontier_size = max(len(frontier), max_frontier_size)

      #pop off cheapest node
      cheapest_element = heapq.heappop(frontier)
      node = cheapest_element[1]
      nodes_expanded += 1

      if not node.state.current_state in visited:
         visited.append(node.state.current_state)
         if node.state.h_cost is 0:
            #Finished, output results
            output_results(initial_state, parent_node, node, nodes_expanded, max_frontier_size)
            return 

         moves = node.state.get_moves()
         for state in moves:
            new_node = Node(state, node)
            heapq.heappush(frontier, (state.g_cost + state.h_cost, new_node))
   pass

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
   default = [
      [2, 3, 0],
      [1, 4, 5],
      [7, 8, 6]
   ]

   return default

def output_results(initial_state, parent_node, result_node, nodes_expanded, max_frontier_size):
   #Finished, output results
   optimal_solution = []

   while not result_node is parent_node:
      optimal_solution.append(result_node.state)
      result_node = result_node.parent_node

   print('Expanding state')
   initial_state.print_state()

   for index in range(len(optimal_solution) - 1, 0, -1):
      state = optimal_solution[index]
      if state.algorithm is 'a_star':
         print('The best state to expand with g(n) + h(n) = {} + {} = {} is...'.format(state.g_cost, state.h_cost, state.g_cost + state.h_cost))
      else:
         print('The best state to expand with g(n) = {} is...'.format(state.g_cost))
      state.print_state()
      print('Expanding this node...\n')
   pass

   print('Goal!!!')
   optimal_solution[0].print_state()
   print('To solve this problem the search algorithm expanded a total of {} nodes'.format(nodes_expanded))
   print('The maximum number of nodes in the queue at any one time: {}'.format(max_frontier_size))
   return 

def algorithm_selection(state):
   print('Enter your choice of algorithm')
   print('1: Uniform Cost Search (Default)')
   print('2. A* with Misplaced Tile Heuristic')
   print('3. A* with the Eucledian Distance Heuristic')
   print('4. [EXIT]')
   selection = input()
   if int(selection) is 2:
      print('A* with Misplaced Tile Heuristic')
      a_star_tile_heuristic_search(state)
      pass
   elif int(selection) is 3:
      print('A* with the Eucledian Distance Heuristic')
      a_star_eucledian_dist_search(state)
      pass
   elif int(selection) is 4:
      return False
   else:
      print('Uniform Cost Search')
      uniform_cost_search(state)

   return True

def main():
   print('Welcome to Kelton\'s (ID: 861234792) 8 puzzle solver')
   selection = input('Type "1" to use a default puzzle, or "2" to enter your own:\n')
   if int(selection) is 2:
      puzzle_set = create_custom_puzzle()
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

def test():
   puzzle_set = create_default_puzzle()
   utility.set_position_dict()
   state = State(puzzle_set, 0, 3, first_state=True)
   state.print_state()
   print(state.g_cost, state.h_cost)

if __name__ == "__main__":
   #test()
   main()
