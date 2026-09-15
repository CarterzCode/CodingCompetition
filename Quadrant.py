"""
Finds the quadrant that a point lies in
Carter Q - September 2026
"""

def main() -> None:
  pass # remove me

  # input
  x: int = int(input())
  y: int = int(input())

  # processing
  if x*y > 0 and x>0 and y>0:
    # output
    print(1)
  elif x*y > 0 and x<0 and y<0:
    print(3)
  elif x<0:
    print(2)
  else:
    print(4)
  


if __name__ == "__main__":
  main()
    
