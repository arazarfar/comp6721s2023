# -*- coding: utf-8 -*-
"""Lab2_Q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Byqnjq9l5rMdqUtk6-vcuIemhJ9JRG76

Concordia COMP 6721 Summer 2023 <br>
Lab Assignment 2 State Space Search (sample implementation) <br>
Question 3
"""

def get_state_children (s, n_rows, n_cols):
  '''
  Inputs:
    s: (i,j) state variable where i,j in [1, 4] 
  Outputs:
        List of children (next states) reachable from state s

  returns the list of states which can be reached from this state with a legal action
  '''
  i,j = s
  children_tmp = [(i,j+1),(i,j-1),(i+1,j), (i-1,j)]
  # For the cells on the border, some actions are not allowed
  children = [item for item in children_tmp if item[0]>=1 and item[0]<=n_rows and item[1]>=1 and item[1]<=n_cols]
  return children

"""DFS Implementation

"""

N_ROWS = 4
N_COLS = 4

start_state = (1,1)
goal_state = (4,4)
closed_states = [] # Visited nodes
open_states  = [start_state] # Queue: To be visited
success = 0 
illegal_states = [(2,2),(2,4),(3,4),(4,1)] 

while open_states:
    x_states = open_states.pop(0)
    print ('Just visited state: ', x_states )
    if x_states == goal_state:
      success =1 
      break
    else:
      closed_states.append(x_states)
      for child in get_state_children(x_states, N_ROWS, N_COLS):
        if child not in illegal_states and child not in closed_states and child not in open_states:
          open_states.insert(0, child)

    print('closed_states: ', closed_states)
    print('open_states: ', open_states, '\n')

if success:
  print('SUCCESS')
else:
  print('FAILUER')

"""BFS Implementation"""

N_ROWS = 4
N_COLS = 4

start_state = (1,1)
goal_state = (4,4)
closed_states = [] # Visited nodes
open_states  = [start_state] # Queue: To be visited
success = 0 
illegal_states = [(2,2),(2,4),(3,4),(4,1)] 

while open_states:
    x_states = open_states.pop(0)
    print ('Just visited state: ', x_states )
    if x_states == goal_state:
      success =1 
      break
    else:
      closed_states.append(x_states)
      for child in get_state_children(x_states, N_ROWS, N_COLS):
        if child not in illegal_states and child not in closed_states and child not in open_states:
          open_states.append(child)

    print('closed_states: ', closed_states)
    print('open_states: ', open_states, '\n')

if success:
  print('SUCCESS')
else:
  print('FAILUER')