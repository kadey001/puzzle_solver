class Tree():
   def __init__(self, root):
      self.root = root
      self.curr_state = None
      self.left = None
      self.right = None
      self.up = None
      self.down = None
   
   def add_node(self, state):
      if node.state.last_move is 'u':
         self.up = state
      elif node.state.last_move is 'd':
         self.down = state
      elif node.state.last_move is 'l':
         self.left = state
      else:
         self.right = state

   def get_cheapest_child(self):
      pass
