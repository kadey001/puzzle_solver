"""
Kelton Adey
Eight-Puzzle Using:
1. Uniform Cost Search
2. A* with Misplaced Tile Heuristic
3. A* with the Eucledian Distance Heuristic
"""

import sys, heapq, utility
from state import State
from tree import Tree

class Node():
   def __init__(self, state, parent_state):
      self.state = state
      self.parent_state = parent_state

def uniform_cost_search(initial_state):
   #tree = Tree(initial_state)
   max_frontier_size, nodes_expanded = 0, 0
   visited = []
   #(g(n)/total_cost, node, path)
   parent_node = Node(initial_state, initial_state)
   frontier = []
   heapq.heappush(frontier, (0, parent_node))

   while frontier:
      #Upade max_frontier_nodes
      print('==============================')
      max_frontier_size = max(len(frontier), max_frontier_size)
      # print(frontier)
      # for item in frontier:
      #    print(item)

      #pop off cheapest node
      g_cost, node = heapq.heappop(frontier)
      nodes_expanded += 1
      # node.state.print_state()
      print('g(n) = {} | h(n) = {}'.format(g_cost, node.state.h_cost))

      if not node.state.current_state in visited:
         visited.append(node.state.current_state)
         node.state.print_state()
         if node.state.h_cost is 0:
            #Finished
            print('To solve this problem the search algorithm expanded a total of {} nodes'.format(nodes_expanded))
            print('The maximum number of nodes in the queue at any one time: {}'.format(max_frontier_size))
            return 

         moves = node.state.get_moves()
         for state in moves:
            new_node = Node(state, node)
            heapq.heappush(frontier, (state.g_cost, new_node))

def a_star_tile_heuristic_search(initial_state):
   pass

def a_star_eucledian_dist_search(initial_state):
   pass

def create_custom_puzzle():
   def number_to_wordth(n):
      ones = ["", "first ","second ","third ","fourth ", "fifth ", "sixth ","seventh ","eighth ","ninth ","tenth ","eleventh ","twelveth ", "thirteenth ", "fourteenth ", "fifteenth ","sixteenth ","seventeenth ", "eighteenth ","nineteenth "]
      twenties = ["","","twentieth ","thirtieth ","fortieth ", "fiftieth ","sixtieth ","seventieth ","eightieth ","ninetieth "]
      thousands = ["","thousandth ","millionth ", "billionth ", "trillionth ", "quadrillionth ", "quintillionth ", "sextillionth ", "septillionth ","octillion ", "nonillionth ", "decillionth ", "undecillionth ", "duodecillionth ", "tredecillionth ", "quattuordecillionth ", "quindecillionth ", "sexdecillionth ", "septendecillionth ", "octodecillionth ", "novemdecillionth ", "vigintillionth "]
      def num999(n):
         c = n % 10 # singles digit
         b = ((n % 100) - c) / 10 # tens digit
         a = ((n % 1000) - (b * 10) - c) / 100 # hundreds digit
         t = ""
         h = ""
         if a != 0 and b == 0 and c == 0:
            t = ones[a] + "hundred "
         elif a != 0:
            t = ones[a] + "hundred and "
         if b <= 1:
            h = ones[n%100]
         elif b > 1:
            h = twenties[b] + ones[c]
         st = t + h
         return st
      def num2word(num):
         if num == 0: return 'zero'
         i = 3
         n = str(num)
         word = ""
         k = 0
         while(i == 3):
            nw = n[-i:]
            n = n[:-i]
            if int(nw) == 0:
                  word = num999(int(nw)) + thousands[int(nw)] + word
            else:
                  word = num999(int(nw)) + thousands[k] + word
            if n == '':
                  i = i+1
            k += 1
         return word[:-1]
      return num2word(n)
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
   print('Enter the first row:\n')
   rows = []
   rows.append([int(x) for x in sys.stdin.readline().split()])
   for i in range(1,len(rows[0])):
      print('Enter the {} row:\n'.format(number_to_wordth(i+1)))
      rows.append([int(x) for x in sys.stdin.readline().split()])

   return rows

def create_default_puzzle():
   """
   Creates a default starting puzzle
   """
   default = [
      [1, 2, 3],
      [0, 4, 5],
      [7, 8, 6]
   ]

   return default

def algorithm_selection(state):
   print('Enter your choice of algorithm')
   print('1: Uniform Cost Search (Default)')
   print('2. A* with Misplaced Tile Heuristic')
   print('3. A* with the Eucledian Distance Heuristic')
   print('4. [EXIT]')
   selection = input()
   if int(selection) is 2:
      print('A* with Misplaced Tile Heuristic')
      pass
   elif int(selection) is 3:
      print('A* with the Eucledian Distance Heuristic')
      pass
   elif int(selection) is 4:
      return False
   else:
      print('Uniform Cost Search')
      uniform_cost_search(state)
      pass

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
   state = State(puzzle_set)
   state.print_state()

   keep_running = True
   while(keep_running):
      keep_running = algorithm_selection(state)

if __name__ == "__main__":
   main()
