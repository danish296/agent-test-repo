# abc.py

def add(a, b):
  # This function is intentionally wrong
  return a - b

def main():
  result = add(5, 3)
  # Expected output is 8, but this will print 2
  print(f"The result is: {result}")

if __name__ == "__main__":
  main()
