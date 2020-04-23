"""
Kelton Adey
Eight-Puzzle Using:
1. Uniform Cost Search
2. A* with Misplaced Tile Heuristic
3. A* with the Eucledian Distance Heuristic
"""

import sys

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
   def __init__(self, initial_state):
      self.initial_state = initial_state
      self.current_state = initial_state
      self.history = []

   def print_state(self):
      """
      Prints out the current state of the puzzle
      """
      for row in self.current_state:
         row_str = '|'
         for item in row:
            row_str += (str(item) + '|')
         print(row_str)
      print('')
   
   def update_state(self, updated_state, action):
      """
      Updates the current state of the puzzle
      """
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

   print('Enter your choice of algorithm')
   print('1: Uniform Cost Search (Default)')
   print('2. A* with Misplaced Tile Heuristic')
   print('3. A* with the Eucledian Distance Heuristic')
   selection = input()
   if int(selection) is 2:
      print('A* with Misplaced Tile Heuristic')
      pass
   elif int(selection) is 3:
      print('A* with the Eucledian Distance Heuristic')
      pass
   else:
      print('Uniform Cost Search')
      pass

if __name__ == "__main__":
   main()