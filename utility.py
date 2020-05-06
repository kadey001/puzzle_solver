position_dict = {}
goal_state = []

def set_position_dict(n = 3):
   """
   Creates a dict for each value's correct position and builds
   a goal state for goal checking
   """
   value = 1
   for i in range(n):
      row = []
      for j in range(n):
         if (i + 1) * (j + 1) >= n**2:
            position_dict[0] = (i, j)
            row.append(0)
         else:
            position_dict[value] = (i, j)
            row.append(value)
            value += 1
      goal_state.append(row)
   