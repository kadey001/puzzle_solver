"""
Kelton Adey
Eight-Puzzle Using:
1. Uniform Cost Search
2. A* with Misplaced Tile Heuristic
3. A* with the Eucledian Distance Heuristic
"""

import sys

def uniform_cost_search(state):
   misplaced_dict = state.misplaced_dict
   costs_dict = state.cost_dict
   print(costs_dict, misplaced_dict)

def get_position_dict(n = 3):
   """Creates a dict for each value's correct position"""
   position_dict = {}
   value = 1
   for i in range(n):
      for j in range(n):
         if i * j >= n**2:
            position_dict[0] = (i, j)
            return position_dict
         else:
            position_dict[value] = (i, j)
            value += 1
   return position_dict

class Node:
   def __init__(self, value = None, left = None, right = None):
      self.value = value
      self.left = left
      self.right = right

class Tree:
   def __init__(self, root):
      self.root = root

   def insert(self):
      pass

class State:
   def __init__(self, initial_state, n = 3):
      self.initial_state = initial_state
      self.current_state = initial_state
      self.history = []
      self.n = n
      self.set_misplaced_dict()
      self.set_cost_dict()

   def print_state(self):
      """Prints out the current state of the puzzle"""
      for row in self.current_state:
         row_str = '|'
         for item in row:
            row_str += (str(item) + '|')
         print(row_str)
      print('')

   def set_misplaced_dict(self):
      """
      Sets up a dictionay with tuples that gives all of the 
      positions for each misplaced square in the puzzle {key=value, (row, colum)}
      """
      misplaced_dict = {}
      expected_value = 1
      #go in order from 1 to end to find the values that are misplaced
      for row, row_item in enumerate(self.current_state):
         for colum, value in enumerate(row_item):
            if int(value) is 0:
               #ignore empty tile
               pass
            elif int(value) is not expected_value:
               misplaced_dict[int(value)] = (row, colum)
            
            expected_value += 1
      
      self.misplaced_dict = misplaced_dict

   def set_cost_dict(self):
      """
      Finds all the costs for each misplaced square and adds them to a cost dictionary
      with the keys being the square values {key=value, cost}
      """
      position_dict = get_position_dict(self.n)
      cost_dict = {}
      for key in self.misplaced_dict:
         #(row, colum, value) of a misplaced element
         misplaced_item_position = self.misplaced_dict[key]

         misplaced_row = misplaced_item_position[0]
         misplaced_colum = misplaced_item_position[1]

         expected_item_position = position_dict[key]
         correct_row = expected_item_position[0]
         correct_colum = expected_item_position[1]

         #Find the cost for moving to correct position and add it to the cost_dict
         cost = abs(misplaced_row - correct_row) + abs(misplaced_colum - correct_colum)
         cost_dict[key] = cost
      
      self.cost_dict = cost_dict

   def update_state(self, updated_state, action):
      """Updates the current state of the puzzle"""
      self.current_state = updated_state
      self.history.append(action)

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
      ['1', '2', '3'],
      ['4', '5', '6'],
      ['8', '7', '0']
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
