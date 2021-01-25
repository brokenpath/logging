import time

import sys 
  
  
def print_to_stderr(*a): 
  
    # Here a is the array holding the objects 
    # passed as the arguement of the function 
    print(*a, file = sys.stderr) 


if __name__ == "__main__":
   i = 0
   while i < 5000:
      print_to_stderr('The program says {}'.format(i))
      i = i + 1
      time.sleep(5)
