import copy

CONST_PUZZLE_SIZE = 3

#Set up a dictionary for the size of the puzzle that has the correct location for each number
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

position_dict = get_position_dict(CONST_PUZZLE_SIZE)

class State:
   def __init__(self, initial_state, prev_cost = 0, n = 3, last_move = None, parent_state = None):
      #Declaring variables
      self.current_state = initial_state
      self.n = n
      self.g_cost = prev_cost
      self.last_move = last_move
      self.parent_state = parent_state
      self.misplaced_dict = {}
      self.cost_dict = {}
      self.hash = 0
      #Calling functions
      self.set_misplaced_dict()
      self.set_cost_dict()
      self.h_cost = self.get_heuristic()
      self.update_cost()
      #print(self.cost_dict)

   def update_cost(self):
      """Updates current state's total cost with its cost + prev cost"""
      self.g_cost += self.h_cost

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
      expected_value = 1
      #go in order from 1 to end to find the values that are misplaced
      for row, row_item in enumerate(self.current_state):
         for colum, value in enumerate(row_item):
            if value is 0:
               #ignore empty tile but store location
               self.empty_tile_location = (row, colum)
               pass
            elif value is not expected_value:
               self.misplaced_dict[value] = (row, colum)
            
            expected_value += 1
            self.hash += (expected_value + 15) * value

   def set_cost_dict(self):
      """
      Finds all the costs for each misplaced square and adds them to a cost dictionary
      with the keys being the square values {key=value, cost}
      """
      
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
         self.cost_dict[key] = cost

   def get_heuristic(self):
      return sum(self.cost_dict.values())

   #Operators
   def move_down(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0] + 1][self.empty_tile_location[1]]
      state_copy[self.empty_tile_location[0] + 1][self.empty_tile_location[1]] = 0
      return State(state_copy, self.g_cost, last_move='d')

   def move_up(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0] - 1][self.empty_tile_location[1]]
      state_copy[self.empty_tile_location[0] - 1][self.empty_tile_location[1]] = 0
      return State(state_copy, self.g_cost, last_move='u')

   def move_right(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] + 1]
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] + 1] = 0
      return State(state_copy, self.g_cost, last_move='r')

   def move_left(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] - 1]
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] - 1] = 0
      return State(state_copy, self.g_cost, last_move='l')

   def get_moves(self):
      """Gives list of all possible move states that can be made from the empty tile's location"""
      moves = []
      L, R, U, D = False, False, False, False
      #print('Empty Tile Location = {}'.format(self.empty_tile_location))
      #Check vertical limits
      if self.empty_tile_location[0] is 0:
         #can't move up
         D = True
      elif self.empty_tile_location[0] is self.n - 1:
         #can't move down
         U = True
      else: 
         #Can move up and down
         U, D = True, True

      #Check horizontal limits
      if self.empty_tile_location[1] is 0:
         #Can't move left
         R = True
      elif self.empty_tile_location[1] is self.n - 1:
         #Can't move right
         L = True
      else:
         #Can move left and right
         L, R = True, True

      #print(U, D, L, R)

      if U:
         moves.append(self.move_up())
      if D:
         moves.append(self.move_down())
      if L:
         moves.append(self.move_left())
      if R:
         moves.append(self.move_right())

      return moves
