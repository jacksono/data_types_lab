#!/usr/bin/env/ python3

def data_type(arg):

  '''Function takes one arument and returns results based on that argument
  
  Args:
      arg: can be a string or list or boolean or an integer
  
  Returns:
      For strings, returns its length.
      For None returns string 'no value'
      For booleans returns the boolean
      For integers returns a string showing how it compares to hundred
      For lists return the 3rd item, or None if it the 3rd item doesn't exist
  '''
  if isinstance(arg, str): #check arg for string
      return len(arg)
  elif isinstance(arg, type(None)): #check arg for None
      return 'no value'
  elif isinstance(arg, bool): #check arg for bool
      return arg
  elif isinstance(arg, int): #check arg for int
      if arg < 100:
          return'less than 100'
      elif arg == 100:
          return 'equal to 100'
      else:
          return 'more than 100'
  elif isinstance(arg, list): #check arg for list
      if len(arg) >= 3:
          return arg[2]
      else:
          return None
  else:
      return 'invalid input' #if none of the describe types is found



