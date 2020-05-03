"""
Kelton Adey
Eight-Puzzle Using:
1. Uniform Cost Search
2. A* with Misplaced Tile Heuristic
3. A* with the Eucledian Distance Heuristic
"""

import sys, queue

from state import State

def uniform_cost_search(initial_state):
   misplaced_dict = initial_state.misplaced_dict
   costs_dict = initial_state.cost_dict
   #print(costs_dict, misplaced_dict)
   #print(initial_state.get_heuristic())

   q = queue.Queue()

   swaps = initial_state.get_swaps()
   for item in swaps:
      item.print_state()

   #root = Node(initial_state)
   #Add all children for current frontier

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
   print('Enter your puzzle, use a zero to represent the blank space')
   print('Enter the first row, use spaces/tabs between numbers:\n')
   row1 = sys.stdin.readline().split()
   print('Enter the second row, use spaces/tabs between numbers:\n')
   row2 = sys.stdin.readline().split()
   print('Enter the third row, use spaces/tabs between numbers:\n')
   row3 = sys.stdin.readline().split()

   return [row1, row2, row3]

def create_default_puzzle():
   """
   Creates a default starting puzzle
   """
   default = [
      [1, 2, 3],
      [4, 5, 6],
      [8, 0, 7]
   ]

   return default

def main_loop(state):
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
   state = State(puzzle_set)
   state.print_state()

   keep_running = True
   while(keep_running):
      keep_running = main_loop(state)

def test():
   test_dict = get_position_dict()
   print(test_dict)

if __name__ == "__main__":
   main()
