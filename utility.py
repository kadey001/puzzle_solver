position_dict = {}

def set_position_dict(n = 3):
   """Creates a dict for each value's correct position"""
   value = 1
   for i in range(n):
      for j in range(n):
         if i * j >= n**2:
            position_dict[0] = (i, j)
         else:
            position_dict[value] = (i, j)
            value += 1
   