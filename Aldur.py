"""
Finds the youngest friend
Carter Q - September 2026
"""

def main() -> None:

  # input
  n: int = int(input())
  age: int
  youngest: int = 190237592
  # processing
  for _ in range(n):
    age = int(input())
    if age < youngest:
      youngest = age
  print(youngest)
  # output


if __name__ == "__main__":
  main()
    
