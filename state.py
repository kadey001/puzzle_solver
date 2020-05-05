import copy, utility, math

class State:
   def __init__(self, initial_state, prev_cost = 0, n = 3, last_move = None, parent_state = None,
      first_state = None, heuristic = None, algorithm = None):
      #Declaring variables
      self.current_state = initial_state
      self.n = n
      self.g_cost = prev_cost
      self.last_move = last_move
      self.parent_state = parent_state
      self.first_state = first_state
      self.heuristic = heuristic
      self.algorithm = algorithm
      self.misplaced_dict = {}
      self.cost_dict = {}
      self.num_misplaced = 0
      #Calling settup functions
      self.set_misplaced_dict()
      self.set_cost_dict()
      self.h_cost = self.get_h_cost()
      self.update_cost()

   def update_cost(self):
      """Updates current state's total cost with its cost + prev cost"""
      if not self.first_state:
         if self.algorithm is 'a_star':
            self.g_cost += 1
         elif self.algorithm is 'uniform':
            self.g_cost += self.h_cost

   def get_h_cost(self):
      if self.heuristic is 'misplaced_tiles':
         return self.num_misplaced
      else:
         return sum(self.cost_dict.values())

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
               self.num_misplaced += 1
            
            expected_value += 1

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

         expected_item_position = utility.position_dict[key]
         correct_row = expected_item_position[0]
         correct_colum = expected_item_position[1]

         #Find the cost for moving to correct position and add it to the cost_dict (using the heuristic type)
         if self.heuristic is 'eucledian':
            cost = math.sqrt((misplaced_row - correct_row)**2 + (misplaced_colum - correct_colum)**2)
         else:
            cost = abs(misplaced_row - correct_row) + abs(misplaced_colum - correct_colum)
         self.cost_dict[key] = cost

   #Operator Functions create and return a state for a given move
   def move_down(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0] + 1][self.empty_tile_location[1]]
      state_copy[self.empty_tile_location[0] + 1][self.empty_tile_location[1]] = 0
      return State(state_copy, self.g_cost, len(self.current_state), last_move='d', heuristic=self.heuristic, algorithm=self.algorithm)

   def move_up(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0] - 1][self.empty_tile_location[1]]
      state_copy[self.empty_tile_location[0] - 1][self.empty_tile_location[1]] = 0
      return State(state_copy, self.g_cost, len(self.current_state),last_move='u', heuristic=self.heuristic, algorithm=self.algorithm)

   def move_right(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] + 1]
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] + 1] = 0
      return State(state_copy, self.g_cost, len(self.current_state), last_move='r', heuristic=self.heuristic, algorithm=self.algorithm)

   def move_left(self):
      state_copy = copy.deepcopy(self.current_state)
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1]] = state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] - 1]
      state_copy[self.empty_tile_location[0]][self.empty_tile_location[1] - 1] = 0
      return State(state_copy, self.g_cost, len(self.current_state), last_move='l', heuristic=self.heuristic, algorithm=self.algorithm)

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
