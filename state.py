import copy

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

class State:
   def __init__(self, initial_state, n = 3):
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
               #ignore empty tile but store location
               self.empty_tile_location = (row, colum)
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

   def get_heuristic(self):
      return sum(self.cost_dict.values())

   def move_down(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0] + 1][self.empty_tile_location[1]]
      state_copy[self.empty_tile_location[0] + 1][self.empty_tile_location[1]] = 0
      return State(state_copy)

   def move_up(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0] - 1][self.empty_tile_location[1]]
      state_copy[self.empty_tile_location[0] - 1][self.empty_tile_location[1]] = 0
      return State(state_copy)

   def move_right(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] + 1]
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] + 1] = 0
      return State(state_copy)

   def move_left(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] - 1]
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] - 1] = 0
      return State(state_copy)

   def get_swaps(self):
      """Gives list of all possible swap states that can be made from the empty tile's location"""
      swaps = []
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

      if U:
         swaps.append(self.move_up())
      if D:
         swaps.append(self.move_down())
      if L:
         swaps.append(self.move_left())
      if R:
         swaps.append(self.move_right())

      return swaps

   def update_state(self, updated_state, action):
      """Updates the current state of the puzzle"""
      self.current_state = updated_state
      self.history.append(action)