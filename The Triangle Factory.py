"""
Finds what type of triangle a triangle is
Carter Q - Setpember 2026
"""

def main() -> None:
  angle_total: int = 0

  # input
  # processing
   # output
  for _ in range(3):
    angle: int = int(input())
    if angle == 90:
      print("Ratvinklig Triangel")
      return
    elif angle > 90:
        print("Trubbig Triangel")
        return
    
  print("Spetsig Triangel")
        

if __name__ == "__main__":
  main()
    
